from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Reading the data---------------------------------------------------
#--------------------------------------------------------------------
fname = "Exoplanets_coordinates.txt"

print('Reading from:', fname)

try:
    fin = open(fname, 'r')
except:
    print('File cannot be opened:', fname)
    exit()

Xly = list()
Yly = list()
Zly = list()

Xpx = list()
Ypx = list()
Zpx = list()

for line in fin :
    coordinates = line.split()
    Xly.append((float(coordinates[0])))
    Yly.append((float(coordinates[1])))
    Zly.append((float(coordinates[2])))

for i in range(len(Xly)) :
    Xpx.append(1000 * (Xly[i]/68000) + 1000)
    Ypx.append(1000 * (-Yly[i]/68000) + 1000)
    Zpx.append(1000 * (Zly[i]/68000) + 1000)

# Load the image
image = Image.open("Artist's_impression_of_the_Milky_Way_gna2.jpg")

# Operating on data--------------------------------------------------
#--------------------------------------------------------------------
# Create a new image object for drawing
print('Operating')

draw = ImageDraw.Draw(image)

# Draw a red dot at each coordinate
for dot in range(len(Xpx)):
    draw.ellipse((Xpx[dot] - 2, 
                  Ypx[dot] - 2, 
                  Xpx[dot] + 2, 
                  Ypx[dot] + 2), 
                  fill="springgreen")

# Writing in exit file-----------------------------------------------
#--------------------------------------------------------------------
print('Saving: MW_dots.jpg')

image.save("MW_dots.jpg")

print('Done')