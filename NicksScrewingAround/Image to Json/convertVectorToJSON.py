# adapted from linedraw.py

from random import *
import math
import argparse
import json
import time
import sys
import os


from PIL import Image, ImageDraw, ImageOps


def convertVectorToJSON(lines):
    '''
        print('Set the root path')
        root_path = getPath('',setRootPath=True)

        print('Set the export file name + path')
        export_path = getPath(root_path)

        print('Set the svg folder')
        svg_folder = getPath(root_path)

        print('Set the json folder')
        json_folder = getPath(root_path)

        print('Set the image name')
        imageFilePath = getPath(root_path)
        '''
    root_path = "C:\\Users\\ncard\\OneDrive - University of Ottawa\\Documents\\GitHub\\csi4103-project\\NicksScrewingAround\\FileIO"
    export_path = root_path + '\\' + 'SVG\\test.svg'
    svg_folder = root_path + '\\' + 'SVG'
    json_folder = root_path + '\\' + 'JSON'
    imageFilePath = root_path + '\\' + 'IMAGE\\basic-shapes.jpg'
    imageFilePath = root_path + '\\' + 'IMAGE\\africa.jpg'
    imageFilePath = root_path + '\\' + 'IMAGE\\africaSmaller.jpg'
    imageFilePath = root_path + '\\' + 'IMAGE\\africaEvenSmaller.jpg'
    no_cv = False

def image_to_json(
    image_filename, lines
    ):


    filename = json_folder + '//' + image_filename + ".json"
    lines_to_file(lines, filename)

def lines_to_file(lines, filename):
    with open(filename, "w") as file_to_save:
        json.dump(lines, file_to_save, indent=4)
