import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import skimage.io as sio
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

# Operating on data--------------------------------------------------
#--------------------------------------------------------------------

# Create scatter plot
scatter = go.Scatter3d(x = Xly, 
                       y = Yly, 
                       z = Zly, 
                       mode = 'markers',
                       marker = dict(size = 3, 
                                     color = 'green',
                                     #symbol = 'species',
                                     opacity = 0.5)
                        )

# Create surface for image overlay
x_range = [-34000, 34000]
y_range = [-34000, 34000]
z_range = [-34000, 34000]

xx, yy = np.meshgrid(np.linspace(x_range[0], x_range[1], 100), 
                     np.linspace(y_range[0], y_range[1], 100))
zz = np.full(xx.shape, 0)

surface = go.Surface(x = xx, 
                     y = yy, 
                     z = zz,
                     colorscale = [[0, 'rgba(0, 0, 0, 0.5)'], 
                                   [1, 'rgba(255, 255, 255, 0.5)']])

#--------------------------------------------------------------------
# Create layout and figure
layout = go.Layout(
    scene = dict(
        xaxis = dict(nticks = 4, range = x_range),
        yaxis = dict(nticks = 4, range = y_range),
        zaxis = dict(nticks = 4, range = z_range),
    )
)

fig = go.Figure(data = [scatter, surface], layout = layout)

#--------------------------------------------------------------------
pyLogo = Image.open("Artist's_impression_of_the_Milky_Way_gna2.jpg")

fig.add_layout_image(
        dict(
            source=pyLogo,
            xref="x",
            yref="y",
            x=-1,
            y=4,
            sizex=4,
            sizey=4,
            sizing="stretch",
            opacity=0.5,
            layer="below")
)

fig.update_layout(
    images = [dict(
        source = pyLogo,
        x = x_range[0],
        sizex = x_range[1] - x_range[0],
        y = y_range[1],
        sizey = y_range[1] - y_range[0],
        xref = "x",
        yref = "y",
        sizing = "stretch",
        opacity = 0.5,
        layer = "below"
    )]
)

fig.write_html ("grafico_3d.html")

fig.show()