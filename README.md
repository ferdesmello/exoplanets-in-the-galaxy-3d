# Exoplanets in the Galaxy

## Overview
Thousands of exoplanets have been discovered, most of them close to us. This distribution is mostly because the methods used for detection can more easily detect exoplanets close to us or exoplanets with certain characteristics, not because all exoplanets are distributed close to us. Curious about what area of our Galaxy we were able to map for exoplanets, I made this interactive visualization. You may see that, until now, we just mapped a very small region of our Galaxy.
Access the interactive visualization in your browser going [here](https://ferdesmello.github.io/exoplanets-in-the-galaxy-3d/). Also, the files are being update monthly with the newly discovered exoplanets in the [exoplanet archive](https://exoplanetarchive.ipac.caltech.edu/). 

![Update Exoplanet Data](https://github.com/your-username/your-repo-name/actions/workflows/your-workflow-file.yml/badge.svg)

Date of the last automatic update: <!--LAST_UPDATE-->2025-06-01<!--END_LAST_UPDATE-->

## What the code does

### 1. Scraping the data
Run **exoplanet_data_from_API.py** to retrieve data from [https://exoplanetarchive.ipac.caltech.edu](https://exoplanetarchive.ipac.caltech.edu) and build (or update) _Exoplanets_coordinates.txt_ and _exoplanets_coordinates_methods.txt_ with distance, position, and method of detection of every exoplanet discovered till now.

### 2. Simple face-on flat map
Run **flat_galaxy_map.py** to retrieve data from _exoplanets_coordinates.txt_ and _Artist's_impression_of_the_Milky_Way_gna_small.jpg_ to make _MW_dots.jpg_, a 2D "map" of the distribution of exaplanets discovered in our Galaxy.
![Representation of the positions of the discovered exoplanets in our Galaxy.](/MW_dots.jpg)

### 3. From TXT to JSON
Run **TXT_to_JSON.py** to retrieve data from _exoplanets_coordinates.txt_ and _exoplanets_coordinates_methods.txt_ and transform the data to JSON format in _exoplanets_coordinates.json_ and _exoplanets_coordinates_methods.json_. This is used in the interactive visualization.

### 4. Semi-transparent PNGs
The images _MW_transparent.png_ and _MW_transparent_small.png_ may already be present. If not, you need to run **Exoplanets_in_the_Galaxy_3D.nb** ([Mathematica notebook](https://www.wolfram.com/notebooks/)) to create them and have a 3D visualization of the exoplanets.

### 5. Local visualization
Now, to access the interactive visualization _locally_ in your browser, you need to run **index.html**.

In your computer, open a terminal window and go to the project folder:
```console
cd C:\Git\exoplanets-in-the-galaxy-3d
```
Create a server:
```console
python -m http.server 8000
```
In your browser, go to:
```console
http://127.0.0.1:8000/
```
Close the server in the terminal with:
```console
Ctrl+C
```

## The illustration of our Galaxy
The Illustration for our Galaxy comes from [here](https://www.eso.org/public/images/eso1339g/).

## For exoplanet archive information in retrieving data, see:
### Some documentation
[https://exoplanetarchive.ipac.caltech.edu/applications/DocSet/index.html?doctree=/docs/docmenu.xml&startdoc=item_1_01](https://exoplanetarchive.ipac.caltech.edu/applications/DocSet/index.html?doctree=/docs/docmenu.xml&startdoc=item_1_01)
### How to use TAP and retrieve data
[https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html](https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html)
### And how to choose your table and data on TAP
[https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html](https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html)
