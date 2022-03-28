import cv2
import matplotlib.pyplot as plt

def scale_image(file_name):
	img = cv2.imread("images/" + file_name)
	w = img.shape[1]
	h = img.shape[0]
	print(w, h)
	#cv2.resize(img, (), )

scale_image("africa.jpg")