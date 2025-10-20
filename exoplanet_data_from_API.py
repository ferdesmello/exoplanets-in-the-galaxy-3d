import urllib.request
import json
import ssl
from datetime import datetime
import re
import pandas as pd
import numpy as np

#--------------------------------------------------------------------
# Define the url

service_url = "https://exoplanetarchive.ipac.caltech.edu/"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = service_url
querytap = "/TAP/sync?query="
query = "select+hostname,pl_name,sy_dist,glat,glon,ra,dec,discoverymethod"
ending = "+from+pscomppars&format=json"

url = service_url + querytap + query + ending

#--------------------------------------------------------------------
# Read the data

print("Retrieving:\n", url, "\n")

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved", len(data), "characters\n")

try:
    js = json.loads(data)
except:
    js = None

#--------------------------------------------------------------------
# Convert directly to DataFrame
df = pd.DataFrame(js)

# Keep only relevant columns and rename them
df = df.rename(columns={
    "hostname": "sname",
    "pl_name": "pname",
    "sy_dist": "sdist",
    "glat": "glat",
    "glon": "glon",
    "discoverymethod": "method"
})

# Ensure numeric columns are floats and keep NaNs
df["sdist"] = pd.to_numeric(df["sdist"], errors="coerce")
df["glat"] = pd.to_numeric(df["glat"], errors="coerce")
df["glon"] = pd.to_numeric(df["glon"], errors="coerce")

#--------------------------------------------------------------------
# Print summary statistics

number_of_planets = df['pname'].nunique()
number_of_stars = df['sname'].nunique()
methods_all = df['method'].value_counts()

print(f"Number of exoplanets discovered: {number_of_planets}")
print(f"Number of stars with discovered exoplanets: {number_of_stars}")
print(methods_all, "\n")

# Delete rows with no distance information
df = df.dropna(subset=["sdist"])

planets_with_distance = df['pname'].nunique()
stars_with_distance = df['sname'].nunique()
methods_dist = df['method'].value_counts()

print(f"Number of those exoplanets with distance determined: {planets_with_distance}")
print(f"Number of those stars with distance determined: {stars_with_distance}")
print(methods_dist, "\n")

#--------------------------------------------------------------------
# Operate on data

print("Operating on data")

pctoly = 3.26156 # Convertion of parsec to light years
Dcg = 26000 # Distance of the Solar System to center of the Galaxy in light years

# Going from spherical galactic coordinates to cartesian and rotating
# and 90° counter clockwise in the plane for the images

# Original transformations
df["original_X"] = df["sdist"]*pctoly*np.cos(np.radians(df["glat"]))*np.cos(np.radians(df["glon"]))-Dcg
df["original_Y"] = df["sdist"]*pctoly*np.cos(np.radians(df["glat"]))*np.sin(np.radians(df["glon"]))
df["original_Z"] = df["sdist"]*pctoly*np.sin(np.radians(df["glat"]))

# Apply 90 degrees counter-clockwise rotation:
# new_X = -original_Y
# new_Y = original_X
df["X"] = -df["original_Y"]  # New X is the negative of the original Y
df["Y"] = df["original_X"]   # New Y is the original X
df["Z"] = df["original_Z"]   # Z remains the same
Methods = set(df['method'])

#--------------------------------------------------------------------
# Write in the exit file

fname = "./Data/exoplanets_coordinates.txt"
print("  Writing on:", fname)
selected_columns = ['X', 'Y', 'Z']
df[selected_columns].to_csv(fname, 
                            sep=" ",
                            header=False,  
                            index=False) 

#------------------------------------
fname = "./Data/exoplanets_coordinates_methods.txt"
print("  Writing on:", fname)
selected_columns = ['X', 'Y', 'Z', 'method']
df[selected_columns].to_csv(fname, 
                            sep=";",
                            header=False, 
                            index=False) 

#------------------------------------
fname = "./Data/exoplanets_coordinates_l_b.txt"
print("  Writing on:", fname)
selected_columns = ['glon', 'glat']
df[selected_columns].to_csv(fname, 
                            sep=" ", 
                            header=False, 
                            index=False) 

#--------------------------------------------------------------------
fdate = "./Data/last_update.txt"

# Write the last update time to "last_update.txt"
print("  Writing on:", fdate)

with open(fdate, 'w') as f:
    f.write(f'LAST_UPDATE={datetime.now().date().isoformat()}')

#--------------------------------------------------------------------
fdate = "./README.md"

# Write the last update time to "README.md"
print("  Writing on:", fdate)

# Load README.md
with open(fdate, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = content

#------------------------------------
# number of stars
new_content = re.sub(
    r'<!--STARS-->.*?<!--STARS-->',
    f'<!--STARS-->{number_of_stars}<!--STARS-->',
    new_content
)

#------------------------------------
# number of planets
new_content = re.sub(
    r'<!--EXOPLANETS-->.*?<!--EXOPLANETS-->',
    f'<!--EXOPLANETS-->{number_of_planets}<!--EXOPLANETS-->',
    new_content
)

#------------------------------------
# number of stars with distance
new_content = re.sub(
    r'<!--SDIST-->.*?<!--SDIST-->',
    f'<!--SDIST-->{stars_with_distance}<!--SDIST-->',
    new_content
)

#------------------------------------
# number of planets with distance
new_content = re.sub(
    r'<!--PDIST-->.*?<!--PDIST-->',
    f'<!--PDIST-->{planets_with_distance}<!--PDIST-->',
    new_content
)

#------------------------------------
# update date of last update
today = datetime.now().date().isoformat()
new_content = re.sub(
    r'<!--LAST_UPDATE-->.*?<!--END_LAST_UPDATE-->',
    f'<!--LAST_UPDATE-->{today}<!--END_LAST_UPDATE-->',
    new_content
)

#------------------------------------
with open(fdate, 'w', encoding='utf-8') as f:
    f.write(new_content)


#--------------------------------------------------------------------
print("All done.")