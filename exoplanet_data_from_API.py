import urllib.request
import json
import ssl
import math
from collections import Counter
from datetime import datetime

#--------------------------------------------------------------------
# Define the url

service_url = "https://exoplanetarchive.ipac.caltech.edu/"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = service_url
querytap = "/TAP/sync?query="
query = "select+sy_dist,glat,glon,discoverymethod"
ending = "+from+pscomppars&format=json"

url = service_url + querytap + query + ending


#--------------------------------------------------------------------
# Read the data

print("Retrieving", url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

try:
    js = json.loads(data)
except:
    js = None

# The data (distance, coordinates, technique) we will keep-------------------
sy_dist = list()
glat = list()
glon = list()
meth = list()

count_exoplanets_distance = 0
count_exoplanets_others = 0
for item in js :
    try : # Some distances are "none" and not of our interest (and they will break the appending)
        sy_dist.append(float(item["sy_dist"]))
        glat.append(float(item["glat"]))
        glon.append(float(item["glon"]))
        meth.append(str(item["discoverymethod"]))
        count_exoplanets_distance += 1
    except :
        count_exoplanets_others += 1
        continue

exoplanets = count_exoplanets_distance + count_exoplanets_others
print(f"Number of exoplanets discovered: {exoplanets}")
print(f"Number of exoplanets with distance determined: {count_exoplanets_distance}")
print(Counter(meth))

#--------------------------------------------------------------------
# Operate on data

print("Operating on data")

X = list()
Y = list()
Z = list()
M = list()
Mset = set(meth)

pctoly = 3.26156 # Convertion of parsec to light years
Dcg = 26000 # Distance of the Solar System to center of the Galaxy in light years

# Going from spherical galactic coordinates to cartesian-------------
for item in range(len(sy_dist)) :
    X.append(sy_dist[item]*pctoly*math.cos(math.radians(glat[item]))*math.cos(math.radians(glon[item]))-Dcg)
    Y.append(sy_dist[item]*pctoly*math.cos(math.radians(glat[item]))*math.sin(math.radians(glon[item])))
    Z.append(sy_dist[item]*pctoly*math.sin(math.radians(glat[item])))
    M.append(meth[item])

#--------------------------------------------------------------------
# Write in the exit file

fname = "exoplanets_coordinates.txt"

print("Writing on:", fname)

try:
    fout = open(fname, "w")
except:
    print("File cannot be opened:", fname)
    exit()

for item in range(len(sy_dist)) :
    fout.write(str("{:.3f}".format(X[item]) + " " + str("{:.3f}".format(Y[item])) + " " + str("{:.3f}".format(Z[item])) + "\n"))
# The "{:.3f}".format() inside the str() is to format the float to 3 decimal algarisms

fout.close()

#--------------------------------------------------------------------
fname = "exoplanets_coordinates_methods.txt"

print("Writing on:", fname)

try:
    fout = open(fname, "w")
except:
    print("File cannot be opened:", fname)
    exit()

for item in range(len(sy_dist)) :
    fout.write(str("{:.3f}".format(X[item]) + ";" + str("{:.3f}".format(Y[item])) + ";" + str("{:.3f}".format(Z[item])) + ";" + str("{}".format(M[item])) + "\n"))
# The "{:.3f}".format() inside the str() is to format the float to 3 decimal algarisms

fout.close()

#--------------------------------------------------------------------
# Write the last update time to "last_update.txt"

with open('last_update.txt', 'w') as f:
    f.write(f'LAST_UPDATE={datetime.now().isoformat()}')

#--------------------------------------------------------------------
print("All done.")