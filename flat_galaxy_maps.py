from PIL import Image, ImageDraw

# Reading the data---------------------------------------------------
#--------------------------------------------------------------------
fname_fo = "./data/exoplanets_coordinates.txt"
fname_eo = "./data/exoplanets_coordinates_l_b.txt"

# Load the images
# Illustration of the Milky Way galaxy face on
MW_fo = Image.open("./images/Artist's_impression_of_the_Milky_Way_gna_small.jpg")

# Picture of the Milky Way galaxy edge on (Equirectangular projection)
MW_eo = Image.open("./images/Milky_Way_edge_on.jpg")

# Changing the coordinate system-------------------------------------
#--------------------------------------------------------------------
print('Reading from:', fname_fo)

try:
    fin = open(fname_fo, 'r')
except:
    print('File cannot be opened:', fname_fo)
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

#--------------------------------------------------------------------

print('Reading from:', fname_eo)

try:
    fin = open(fname_eo, 'r')
except:
    print('File cannot be opened:', fname_eo)
    exit()

l = list()
b = list()

lpx_flipped = list()
lpx = list()
bpx = list()

for line in fin :
    coordinates = line.split()
    l.append((float(coordinates[0])))
    b.append((float(coordinates[1])))

# Size of the image in pixels
width = 2000
height = 4000

lpx_flipped = [(((lval + 180) % 360) / 360 * height) for lval in l]
bpx = [((90 - bval) / 180 * width) for bval in b]
lpx = [width * 2 - lx for lx in lpx_flipped]

# Operating on data--------------------------------------------------
#--------------------------------------------------------------------
# Create a new image object for drawing
print('Operating...')

draw = ImageDraw.Draw(MW_fo)

# Draw a green dot at each coordinate
for dot in range(len(Xpx)):
    draw.ellipse((Xpx[dot] - 2, 
                  Ypx[dot] - 2, 
                  Xpx[dot] + 2, 
                  Ypx[dot] + 2), 
                  fill="springgreen")

#--------------------------------------------------------------------
draw = ImageDraw.Draw(MW_eo)

# Draw a green dot at each coordinate
for dot in range(len(lpx)):
    draw.ellipse((lpx[dot] - 2, 
                  bpx[dot] - 2, 
                  lpx[dot] + 2, 
                  bpx[dot] + 2), 
                  fill="springgreen")

# Writing in exit file-----------------------------------------------
#--------------------------------------------------------------------
print('Saving: ./images/MW_fo_dots.jpg and ./images/MW_eo_dots.jpg')

MW_fo.save("./images/MW_fo_dots.jpg")
MW_eo.save("./images/MW_eo_dots.jpg")

#--------------------------------------------------------------------
print('All done.')