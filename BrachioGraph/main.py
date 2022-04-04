import os, numpy, sys
from linedraw import *
from images import json_reader
from brachiograph import BrachioGraph
from array_format import transform_array
import inverse_kinematics as ik


# Lengths of arms in cm (for now)
forearm = 10.4
bicep = 10.0
# gotta figure out if this is actually origin
origin = [0,0]

#This function processes the inputted image into a JSON, a SVG, and a txt
def process_image(processing_image, contours_value=2, hatch_value=0):
    image_to_json(processing_image, draw_contours=contours_value, draw_hatch=hatch_value)
    #image_to_json("africa.jpg", draw_contours=2, draw_hatch=0)
    #This code finds an image with the indicated name in the 'images' directory and:
    #    -draws the contours and hatch lines
    #    -creates a JSON file with the same name
    #    -creates an SVG file with the same name
    #Smaller contour and hatch values give more detail.
    #Recommended values:
    #    countours = 2 (between 0.5 and 4)
    #    draw_hatch = 16 (between 8 and 16)

    #json_data = json_reader.read_json("images/africa.jpg.json")
    json_data = json_reader.read_json("images/" + processing_image + ".json")
    #array_transformed = transform_array(json_data)
    #json_reader.write_to_text(json_data)
    #json_reader.write_to_json(json_data)

    #cwd = os.getcwd()
    #os.chdir(cwd + "/images")
    #cwd = os.getcwd()
    #exec(open('json_reader.py').read())


def draw_image(drawing_image):
    bg = BrachioGraph() #Initializes the brachiograph, "waking it up"
    bg.plot_file(drawing_image) #Tells the brachiograph to draw

if len(sys.argv) == 0:
    print("Please give an image file name for the brachiograph to draw")
    sys.exit()

drawing_image = sys.argv[0] #Finds the name of the image (located in the /images/ directory)

#Checks for a value for the contours (outline). Assigns a default moderate value
if (len(sys.argv) > 1):
    contours_value = sys.argv[1]

    # Checks for a value for the hatching (shading). Assigns no shading by default
    if (len(sys.argv >2)):
        hatch_value = sys.argv[2]
    else:
        hatch_value = 0
else:
    contours_value = 2

process_image(drawing_image, contours_value, hatch_value)
draw_image(drawing_image)