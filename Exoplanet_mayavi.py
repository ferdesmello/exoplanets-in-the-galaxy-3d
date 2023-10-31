from PIL import Image, ImageDraw
import numpy as np
import mayavi.mlab as mlab
from tvtk.api import tvtk

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
image = Image.open("MWtransparent.png")
image2 = Image.open("MWtransparent.png")

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
print('Saving: MWtransparent_dots.png')

image.save("MWtransparent_dots.png")

print('Done')

# 3D plot------------------------------------------------------------
#--------------------------------------------------------------------
# Create a new figure with a black background
mlab.figure(bgcolor=(0, 0, 0), size=(1000, 800))

# Create the scatter plot with green points
mlab.points3d(Xly,
              Yly,
              Zly,
              color=(0, 1, 0),
              scale_factor = 200)

# Load image from disk (replace 'your_image_path.png' with your file path)
image_path = "MWtransparent.png"
image = Image.open(image_path).convert('L')  # Convert to grayscale
img = np.array(image)

# Display the image at z = 0
image_plane = mlab.imshow(img, extent=[-68000, 68000, -68000, 68000, 0, 0])

# Show the plot
mlab.show()

