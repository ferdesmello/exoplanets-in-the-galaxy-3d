import numpy as np
import plotly.graph_objects as go
import skimage.io as sio

x = np.linspace(-2,2, 128)
x, z = np.meshgrid(x,x)
y = np.sin(x**2*z)

fig = go.Figure(go.Surface(x=x, y=y, z=z,
                           colorscale='RdBu', 
                           showscale=False))

image = sio.imread ("https://raw.githubusercontent.com/empet/Discrete-Arnold-map/master/Images/cat-128.jpg") 

print(image.shape)
img = image[:, :, 1] 
Y = 0.5 * np.ones(y.shape)
fig.add_surface(x=x, y=Y, z=z, 
                surfacecolor=np.flipud(img), 
                colorscale='matter_r', 
                showscale=False)
fig.update_layout(width=600, height=600, 
                  scene_camera_eye_z=0.6, 
                  scene_aspectratio=dict(x=0.9, y=1, z=1));
fig.show()