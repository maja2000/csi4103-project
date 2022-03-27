# adapted from linedraw.py

from random import *
import math
import argparse
import json
import time
import sys
import os
import numpy as np
import cv2

from PIL import Image, ImageDraw, ImageOps

def convertImageToVector():
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
    svg_folder =  root_path + '\\' + 'SVG'
    json_folder = root_path + '\\' + 'JSON'
    imageFilePath = root_path + '\\' + 'IMAGE\\basic-shapes.jpg'
    imageFilePath = root_path + '\\' + 'IMAGE\\africa.jpg'
    imageFilePath = root_path + '\\' + 'IMAGE\\africaSmaller.jpg'
    imageFilePath = root_path + '\\' + 'IMAGE\\africaEvenSmaller.jpg'
    no_cv = False

    lines = vectorise(imageFilePath)
    return lines






# -------------- conversion control --------------

def vectorise(
    image_filename, resolution=1024,
    draw_contours=False, repeat_contours=1,
    draw_hatch=False, repeat_hatch=1,
    ):

    image = None
    possible = [
        image_filename,
        "images/"+image_filename,
        "images/"+image_filename+".jpg",
        "images/"+image_filename+".png",
        "images/"+image_filename+".tif"
    ]

    for p in possible:
        try:
            image = Image.open(p)
            #image = Image.open(imageFilePath)
            #image = Image.open(image_path + '\\' + fileName)
            break
        except:
            pass
    #image = Image.open(image_path + '\\' + fileName)
    w,h = image.size

    # convert the image to greyscale
    image = image.convert("L")

    # maximise contrast
    image=ImageOps.autocontrast(image, 10)

    lines = []

    if draw_contours and repeat_contours:
        contours = sortlines(getcontours(
            image.resize((int(resolution/draw_contours), int(resolution/draw_contours*h/w))),
            draw_contours
        ))
        for r in range(repeat_contours):
            lines += contours




    f = open(svg_folder + '//' + image_filename + ".svg", 'w')
    #f = open(svg_folder + fileName + ".svg", 'w')
    f.write(makesvg(lines))
    f.close()
    segments = 0
    for line in lines:
        segments = segments + len(line)
    print(len(lines), "strokes,", segments, "points.")
    print("done.")
    return lines



# -------------- vectorisation options --------------

def getcontours(image, draw_contours=2):
    print("generating contours...")
    image = find_edges(image)
    IM1 = image.copy()
    IM2 = image.rotate(-90,expand=True).transpose(Image.FLIP_LEFT_RIGHT)
    dots1 = getdots(IM1)
    contours1 = connectdots(dots1)
    dots2 = getdots(IM2)
    contours2 = connectdots(dots2)

    for i in range(len(contours2)):
        contours2[i] = [(c[1],c[0]) for c in contours2[i]]
    contours = contours1+contours2

    for i in range(len(contours)):
        for j in range(len(contours)):
            if len(contours[i]) > 0 and len(contours[j])>0:
                if distsum(contours[j][0],contours[i][-1]) < 8:
                    contours[i] = contours[i]+contours[j]
                    contours[j] = []

    for i in range(len(contours)):
        contours[i] = [contours[i][j] for j in range(0,len(contours[i]),8)]


    contours = [c for c in contours if len(c) > 1]

    for i in range(0,len(contours)):
        contours[i] = [(v[0]*draw_contours,v[1]*draw_contours) for v in contours[i]]

    return contours



# -------------- supporting functions for drawing contours --------------

def find_edges(image):
    print("finding edges...")
    if no_cv:
        #appmask(IM,[F_Blur])
        appmask(image,[F_SobelX,F_SobelY])
    else:
        im = np.array(image)
        im = cv2.GaussianBlur(im,(3,3),0)
        im = cv2.Canny(im,100,200)
        image = Image.fromarray(im)
    return image.point(lambda p: p > 128 and 255)


def getdots(IM):
    print("getting contour points...")
    PX = IM.load()
    dots = []
    w,h = IM.size
    for y in range(h-1):
        row = []
        for x in range(1,w):
            if PX[x,y] == 255:
                if len(row) > 0:
                    if x-row[-1][0] == row[-1][-1]+1:
                        row[-1] = (row[-1][0],row[-1][-1]+1)
                    else:
                        row.append((x,0))
                else:
                    row.append((x,0))
        dots.append(row)
    return dots


def connectdots(dots):
    print("connecting contour points...")
    contours = []
    for y in range(len(dots)):
        for x,v in dots[y]:
            if v > -1:
                if y == 0:
                    contours.append([(x,y)])
                else:
                    closest = -1
                    cdist = 100
                    for x0,v0 in dots[y-1]:
                        if abs(x0-x) < cdist:
                            cdist = abs(x0-x)
                            closest = x0

                    if cdist > 3:
                        contours.append([(x,y)])
                    else:
                        found = 0
                        for i in range(len(contours)):
                            if contours[i][-1] == (closest,y-1):
                                contours[i].append((x,y,))
                                found = 1
                                break
                        if found == 0:
                            contours.append([(x,y)])
        for c in contours:
            if c[-1][1] < y-1 and len(c)<4:
                contours.remove(c)
    return contours



# -------------- optimisation for pen movement --------------

def sortlines(lines):
    print("optimizing stroke sequence...")
    clines = lines[:]
    slines = [clines.pop(0)]
    while clines != []:
        x,s,r = None,1000000,False
        for l in clines:
            d = distsum(l[0],slines[-1][-1])
            dr = distsum(l[-1],slines[-1][-1])
            if d < s:
                x,s,r = l[:],d,False
            if dr < s:
                x,s,r = l[:],s,True

        clines.remove(x)
        if r == True:
            x = x[::-1]
        slines.append(x)
    return slines



def lines_to_file(lines, filename):
    with open(filename, "w") as file_to_save:
        json.dump(lines, file_to_save, indent=4)



# -------------- helper functions --------------

def midpt(*args):
    xs,ys = 0,0
    for p in args:
        xs += p[0]
        ys += p[1]
    return xs/len(args),ys/len(args)


def distsum(*args):
    return sum([ ((args[i][0]-args[i-1][0])**2 + (args[i][1]-args[i-1][1])**2)**0.5 for i in range(1,len(args))])

def makesvg(lines):
    print("generating svg file...")
    width = math.ceil(max([max([p[0]*0.5 for p in l]) for l in lines]))
    height = math.ceil(max([max([p[1]*0.5 for p in l]) for l in lines]))
    out = '<svg xmlns="http://www.w3.org/2000/svg" height="%spx" width="%spx" version="1.1">' % (height, width)

    for l in lines:
        l = ",".join([str(p[0]*0.5)+","+str(p[1]*0.5) for p in l])
        out += '<polyline points="'+l+'" stroke="black" stroke-width="1" fill="none" />\n'
    out += '</svg>'
    return out


# Function to get paths instead of hard coding
def getPath(rootPath,setRootPath = False):
    temp_path = input('Enter the path: ')
    if setRootPath == False:
        temp_path = rootPath + '\\' + temp_path

    while not os.path.isdir(temp_path):
        print('The path you entered is invalid')
        print('You entered: ' + temp_path)
        print('Enter dontCare to exit')
        temp_path = input('Enter the path: ')
        if temp_path == 'dontCare':
            break
    return temp_path


F_Blur = {
    (-2,-2):2,(-1,-2):4,(0,-2):5,(1,-2):4,(2,-2):2,
    (-2,-1):4,(-1,-1):9,(0,-1):12,(1,-1):9,(2,-1):4,
    (-2,0):5,(-1,0):12,(0,0):15,(1,0):12,(2,0):5,
    (-2,1):4,(-1,1):9,(0,1):12,(1,1):9,(2,1):4,
    (-2,2):2,(-1,2):4,(0,2):5,(1,2):4,(2,2):2,
}
F_SobelX = {(-1,-1):1,(0,-1):0,(1,-1):-1,(-1,0):2,(0,0):0,(1,0):-2,(-1,1):1,(0,1):0,(1,1):-1}
F_SobelY = {(-1,-1):1,(0,-1):2,(1,-1):1,(-1,0):0,(0,0):0,(1,0):0,(-1,1):-1,(0,1):-2,(1,1):-1}
