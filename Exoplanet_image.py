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
image = Image.open("MWtransparent.png")
image2 = plt.imread("MWtransparent.png") ####

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

# Convert the image to RGBA format
image_rgba = image.convert("RGBA")

# Resize the image for better performance
smaller_dim = (100, 100)
image_resized = image.resize(smaller_dim, Image.ANTIALIAS)
image_resized_array = np.array(image_resized.convert("RGBA"))

# 3D plot------------------------------------------------------------
#--------------------------------------------------------------------

# Create a 3D subplot
fig = plt.figure(figsize = (8, 8))

ax = fig.add_subplot(111, projection = "3d")

# Plot the data
ax.scatter3D(Xly,
             Yly,
             Zly, 
             color = "springgreen",
             marker = "o",
             alpha = 1,
             s = 2)

x_range = [-34000, 34000]
y_range = [-34000, 34000]
z_pos = 0

xx, yy = np.meshgrid(np.linspace(x_range[0], x_range[1], smaller_dim[0]), 
                     np.linspace(y_range[0], y_range[1], smaller_dim[1]))
zz = np.full(xx.shape, z_pos)

ax.plot_surface(xx, 
                yy, 
                zz, 
                rstride=1, 
                cstride=1, 
                facecolors=image_resized_array/255.0, 
                linewidth=0, 
                alpha=1)

# Set labels for the axes
ax.set_xlabel("X [ly]")
ax.set_ylabel("Y [ly]")
ax.set_zlabel("Z [ly]")

ax.set_xlim(-34000, 34000)
ax.set_ylim(-34000, 34000)
ax.set_zlim(-34000, 34000)

fig.savefig("Galaxy.png", dpi=300)

# Show the plot
plt.show()
