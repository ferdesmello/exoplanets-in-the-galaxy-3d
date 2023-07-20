from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PIL import Image

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
    Xpx.append((Xly[i]/68000)*1000+1000)
    Ypx.append((-Yly[i]/68000)*1000+1000)
    Zpx.append((Zly[i]/68000)*1000+1000)

# Load the image
image = Image.open("MWtransparent.png")

# Operating on data--------------------------------------------------
#--------------------------------------------------------------------
# Create a new image object for drawing
print('Operating')

draw = ImageDraw.Draw(image)

# Draw a red dot at each coordinate
for dot in range(len(Xpx)):
    draw.ellipse((Xpx[dot]-2, 
                  Ypx[dot]-2, 
                  Xpx[dot]+2, 
                  Ypx[dot]+2), 
                  fill="springgreen")

# Writing in exit file-----------------------------------------------
#--------------------------------------------------------------------
print('Saving: MWtransparent_dots.png')

image.save("MWtransparent_dots.png")

print('Done')

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

# Load the PNG image
image2 = plt.imread("MWtransparent.png")

# Define the range of x and y values
x_range = np.linspace(-34000, 
                      34000, 
                      image2.shape[1])
y_range = np.linspace(-34000, 
                      34000, 
                      image2.shape[0])

# Create a grid of x and y values
X, Y = np.meshgrid(x_range, y_range)

# Plot the surface with the image
ax.plot_surface(X, 
                Y, 
                np.zeros_like(X), 
                facecolors = image2, 
                shade=False)

# Set labels for the axes
ax.set_xlabel("X [ly]")
ax.set_ylabel("Y [ly]")
ax.set_zlabel("Z [ly]")

ax.set_xlim(-34000, 34000)
ax.set_ylim(-34000, 34000)
ax.set_zlim(-34000, 34000)

"""# Set the interpolation method for the image overlay
ax._facecolors2d = ax._facecolors3d
ax._edgecolors2d = ax._edgecolors3d
ax.dist = 10  # Adjust the distance from the plot"""

fig.savefig("Galaxy.png", dpi=300)

# Show the plot
plt.show()
