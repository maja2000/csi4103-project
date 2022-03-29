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
def process_image(processing_image):
    image_to_json(processing_image, draw_contours=2, draw_hatch=16)
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
    bg = BrachioGraph()
    bg.plot_file(drawing_image)

drawing_image = sys.argv[0]
process_image(drawing_image)
draw_image(drawing_image)