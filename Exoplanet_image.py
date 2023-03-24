from PIL import Image, ImageDraw

#Reading the data----------------------------------------------------
#--------------------------------------------------------------------
fname = "Exoplanets_coordinates.txt"

print('Reading from:', fname)

try:
    fin = open(fname, 'r')
except:
    print('File cannot be opened:', fname)
    exit()

X = list()
Y = list()
#Z = list()
#Coord = list()

for line in fin :
    coordinates = line.split()
    X.append((float(coordinates[0])/68000)*1000+1000)
    Y.append((-float(coordinates[1])/68000)*1000+1000)
    #Z.append((float(coordinates[2])/68000)*1000+1000)
    #Coord = list(zip(X, Y))
    
#print(X, Y)

#Load the image
image = Image.open("MWtransparent.png")
#Operating on data---------------------------------------------------
#--------------------------------------------------------------------
#Create a new image object for drawing
print('Operating')

draw = ImageDraw.Draw(image)

#Draw a red dot at each coordinate
#draw.ellipse((0-10, 0-10, 0+10, 0+10), fill="green")
#draw.ellipse((1000-10, 0-10, 1000+10, 0+10), fill="red")
#draw.ellipse((0-10, 1000-10, 0+10, 1000+10), fill="green")
for dot in range(len(X)):
    draw.ellipse((X[dot]-2, Y[dot]-2, X[dot]+2, Y[dot]+2), fill="springgreen")
    #draw.ellipse((Coord[0]-2, Coord[1]-2, Coord[0]+2, Coord[1]+2), fill="green")
#Writing in exit file------------------------------------------------
#--------------------------------------------------------------------
print('Saving: MWtransparent_dots.png')

image.save("MWtransparent_dots.png")

print('Done')