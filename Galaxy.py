import numpy as np
from pythreejs import *
from IPython.display import display

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

for line in fin :
    coordinates = line.split()
    Xly.append((float(coordinates[0])))
    Yly.append((float(coordinates[1])))
    Zly.append((float(coordinates[2])))

x = np.array(Xly)
y = np.array(Yly)
z = np.array(Zly)
print(x)

# Create scatter plot
points = []
for i in range(len(Xly)):
    geometry = SphereGeometry(radius=0.01)  # Adjust radius as needed
    material = MeshBasicMaterial(color='red')
    point = Mesh(geometry, material, position=[x[i], y[i], z[i]])
    points.append(point)
scatter_plot = Group(children=points)
scatter_plot_material = PointsMaterial(color='green', 
                                       size=0.05)
scatter_plot = Points(scatter_geometry, scatter_plot_material)

# Create x-y plane
xmax, xmin, ymax, ymin = 1, 0, 1, 0
plane_geometry = PlaneGeometry(width=xmax-xmin, height=ymax-ymin)
# load image
image = ImageTexture(imageuri='MWtransparent.png')
# create material
plane_material = MeshBasicMaterial(map=image)
plane = Mesh(geometry=plane_geometry, material=plane_material)

# Position the plane: the plane is initially created on the z-x plane, so we need to rotate it
# Also, we set the z position to the lowest point in our scatter plot
#plane.rotation = [-np.pi/2, 0, 0]
plane.position = [0.5, 0.5, 0]  # replace 0 with min(z) if you want the plane to be below the points

# Create the scene
scene = Scene(children=[scatter_plot, plane, AmbientLight(color='#777777')])

# Setup the camera
camera = PerspectiveCamera(position=[0, 3, 3], up=[0, 0, 1], children=[DirectionalLight(color='white', position=[3, 5, 1], intensity=0.6)])

# Render the scene
renderer = Renderer(camera=camera, background='black', background_opacity=1, scene=scene, controls=[OrbitControls(controlling=camera)])

# Display it
renderer
display(renderer)