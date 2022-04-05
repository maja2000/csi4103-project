import sys
from linedraw import *
from images import json_reader
from brachiograph import BrachioGraph


# Lengths of arms in cm (for now)
forearm = 10.4
bicep = 10.0
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

    json_data = json_reader.read_json("images/" + processing_image + ".json")


def draw_image(drawing_image):
    bg = BrachioGraph() #Initializes the brachiograph, "waking it up"
    bg.plot_file(drawing_image) #Tells the brachiograph to draw

if len(sys.argv) == 1:
    print("Please give an image file name for the brachiograph to draw")
    sys.exit()

drawing_image = sys.argv[1] #Finds the name of the image (located in the /images/ directory)

contours_value = 2
hatch_value = 0

#Checks for a value for the contours (outline). Assigns a default moderate value
if (len(sys.argv) > 2):
    contours_value = sys.argv[2]

    # Checks for a value for the hatching (shading). Assigns no shading by default
    if (len(sys.argv) > 3):
        hatch_value = sys.argv[3]

process_image(drawing_image, contours_value, hatch_value)
draw_image(drawing_image)


##############################################################################
# run this file name and include the name of the image as a system argument
# ex. "python main.py X.jpg"
# X.jpg is considered system argument 1
##############################################################################
#drawing_image = sys.argv[1]

# processing the image using image_to_json()
#process_image(drawing_image)

# drawing the image using plot_file()