import json

#--------------------------------------------------------------------
# Read the text file and split it into lines
with open("exoplanets_coordinates.txt", "r") as f:
    lines = f.readlines()

# Convert each line to a list of coordinates
data = [list(map(float, line.strip().split())) for line in lines]

# Write the data to a JSON file
with open("exoplanets_coordinates.json", "w") as f:
    json.dump(data, f)

#--------------------------------------------------------------------
# Read the text file and split it into lines
with open("exoplanets_coordinates_methods.txt", "r") as f:
    lines = f.readlines()

# Convert each line to a list of coordinates with correct data types
data2 = []
for line in lines:
    parts = line.strip().split(";")
    if len(parts) == 4:  # Ensure there are four parts
        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            label = parts[3]
            data2.append([x, y, z, label])
        except ValueError:
            print(f"Skipping line due to invalid numeric data: {line.strip()}") #report errors and skip.
    else:
        print(f"Skipping line due to incorrect number of fields: {line.strip()}") #report errors and skip.

# Add the Solar System
data2.append([float(-26000.0), float(0.0), float(0.0), "Sun"])

# Write the data to a JSON file
with open("exoplanets_coordinates_methods.json", "w") as f:
    json.dump(data2, f, indent=4) #using indent=4 for better readability