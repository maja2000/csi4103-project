import numpy as np
import matplotlib.pyplot as plt
import os
from linedraw import *
from images import json_reader
from array_format import transform_array
import turtle
from turtle import *

image_to_json("circle_filled.jpg", draw_contours=2, draw_hatch=0)
json_data = json_reader.read_json("images/deathly_hallows.jpg.json")
#image_to_json("africa.jpg", draw_contours=2, draw_hatch=0)
#json_data = json_reader.read_json("images/africa.jpg.json")

turtle.screensize(2048, 3048)

screen = Screen()
screen.setup(width=2048, height=2048)

turtle.penup()
for line in json_data:
	turtle.goto(line[0][0], line[0][1])
	turtle.pendown()
	for coordinate in line:
		turtle.goto(coordinate[0], coordinate[1])
	turtle.penup()

turtle.exitonclick()