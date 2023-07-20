import urllib.request, urllib.parse, urllib.error
import json
import ssl
import math

# Defining the url---------------------------------------------------
#--------------------------------------------------------------------
serviceurl = "https://exoplanetarchive.ipac.caltech.edu/"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input("Enter url (Type Enter to go with the default url): ")
if len(address) < 1: #break
    address = serviceurl

querytap = "/TAP/sync?query="

query = input("Enter query (Type Enter to go with the default query): ")
if len(query) < 1: #break
    query = "select+sy_dist,glat,glon+from+pscomppars&format=json"

url = serviceurl + querytap + query

# Reading the data---------------------------------------------------
#--------------------------------------------------------------------
print("Retrieving", url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

try:
    js = json.loads(data)
except:
    js = None

# The data (distance and coordinates) we will keep-------------------
sy_dist = list()
glat = list()
glon = list()

for item in js :
    try : # Some distances are "none" and not of our interest (and they will break the appending)
        sy_dist.append(float(item["sy_dist"]))
        glat .append(float(item["glat"]))
        glon.append(float(item["glon"]))
    except :
        continue

# Operating on data--------------------------------------------------
#--------------------------------------------------------------------
print("Operating on data")

X = list()
Y = list()
Z = list()

pctoly = 3.26156 # Convertion of parsec to light years
Dcg = 26000 # Distance of the Solar System to center of the Galaxy in light years

# Going from spherical galactic coordinates to cartesian-------------
for item in range(len(sy_dist)) :
    X.append(sy_dist[item]*pctoly*math.cos(math.radians(glat[item]))*math.cos(math.radians(glon[item]))-Dcg)
    Y.append(sy_dist[item]*pctoly*math.cos(math.radians(glat[item]))*math.sin(math.radians(glon[item])))
    Z.append(sy_dist[item]*pctoly*math.sin(math.radians(glat[item])))

# Writing in exit file-----------------------------------------------
#--------------------------------------------------------------------
fname = "Exoplanets_coordinates.txt"

print("Writing on:", fname)

try:
    fout = open(fname, "w")
except:
    print("File cannot be opened:", fname)
    exit()

for item in range(len(sy_dist)) :
    fout.write(str("{:.2f}".format(X[item]) + " " + str("{:.2f}".format(Y[item])) + " " + str("{:.2f}".format(Z[item])) + "\n"))
# The "{:.2f}".format() inside the str() is to format the float to 2 decimal algarisms

fout.close()

print("Done")