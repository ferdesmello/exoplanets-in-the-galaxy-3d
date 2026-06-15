"""
Data Transformer

This script converts exoplanet coordinate data from text format to JSON format.
It processes two files:
1. Basic coordinates (X, Y, Z) - converted to JSON for visualization
2. Coordinates with discovery methods (X, Y, Z, method) - converted to JSON with metadata

The script also adds the Solar System's position at [0, -26000, 0] to the dataset
to provide a reference point for visualization.

Output files are formatted as JSON for easy integration with web-based visualization tools.
"""

import json

#--------------------------------------------------------------------
print('Starting...')

# Read the text file and split it into lines
with open("./data/exoplanets_coordinates.txt", "r") as f:
    lines = f.readlines()

# Convert each line to a list of coordinates
data = [list(map(float, line.strip().split())) for line in lines]

# Write the data to a JSON file
with open("./data/exoplanets_coordinates.json", "w") as f:
    json.dump(data, f)

#--------------------------------------------------------------------
# Read the text file and split it into lines
with open("./data/exoplanets_coordinates_methods.txt", "r") as f:
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
data2.append([float(0.0), float(-26000.0), float(0.0), "Sun"])

# Write the data to a JSON file
with open("./data/exoplanets_coordinates_methods.json", "w") as f:
    json.dump(data2, f, indent=4) #using indent=4 for better readability

#--------------------------------------------------------------------
print('All done.')