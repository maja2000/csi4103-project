#See the attached .txt file
from linedraw import *


image_to_json("africa.jpg", draw_contours=2, draw_hatch=16)
#This code finds an image with the indicated name in the 'images' directory and:
#    -draws the contours and hatch lines
#    -creates a JSON file with the same name
#    -creates an SVG file with the same name
#Smaller contour and hatch values give more detail.
#Recommended values:
#    countours = 2 (between 0.5 and 4)
#    draw_hatch = 16 (between 8 and 16)


#lines = vectorise("Me Strethcing.jpg", draw_hatch=0, draw_contours=0.5)
#This code returns a list of lines, each of which is a list of points
#It also produces an SVG file with those lines