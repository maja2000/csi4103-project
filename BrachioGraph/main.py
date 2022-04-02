import os, numpy, sys
from linedraw import *
from images import json_reader
from brachiograph import BrachioGraph
from array_format import transform_array
import inverse_kinematics as ik


# Lengths of arms in cm (for now)
forearm = 10.4
bicep = 10.0
origin = [0,0]

#This function processes the inputted image into a JSON and a SVG
def process_image(processing_image):
    image_to_json(processing_image, draw_contours=2, draw_hatch=16)

    #This code finds an image with the indicated name in the 'images' directory and:
    #    -draws the contours and hatch lines
    #    -creates a JSON file with the same name
    #    -creates an SVG file with the same name
    #Smaller contour and hatch values give more detail.
    #Recommended values:
    #    countours = 2 (between 0.5 and 4)
    #    draw_hatch = 16 (between 8 and 16)

    json_data = json_reader.read_json("images/" + processing_image + ".json")


def draw_image(drawing_image):
    bg = BrachioGraph()
    bg.plot_file(drawing_image)

##############################################################################
# run this file name and include the name of the image as a system argument
# ex. "python main.py X.jpg"
# X.jpg is considered system argument 1
##############################################################################
drawing_image = sys.argv[1]

# processing the image using image_to_json()
process_image(drawing_image)

# drawing the image using plot_file()
draw_image(drawing_image)