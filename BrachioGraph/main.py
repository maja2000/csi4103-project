import os
from linedraw import *
from images import json_reader

image_to_json("africa.jpg", draw_contours=2, draw_hatch=16)
#This code finds an image with the indicated name in the 'images' directory and:
#    -draws the contours and hatch lines
#    -creates a JSON file with the same name
#    -creates an SVG file with the same name
#Smaller contour and hatch values give more detail.
#Recommended values:
#    countours = 2 (between 0.5 and 4)
#    draw_hatch = 16 (between 8 and 16)

json_data = json_reader.read_json("images/africa.jpg.json")
json_reader.write_to_text(json_data)

#cwd = os.getcwd()
#os.chdir(cwd + "/images")
#cwd = os.getcwd()
#exec(open('json_reader.py').read())

