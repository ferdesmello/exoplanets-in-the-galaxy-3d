import json

# Read the text file and split it into lines
with open("Exoplanets_coordinates.txt", "r") as f:
    lines = f.readlines()

# Convert each line to a list of coordinates
data = [list(map(float, line.strip().split())) for line in lines]

# Write the data to a JSON file
with open("Exoplanets_coordinates.json", "w") as f:
    json.dump(data, f)
