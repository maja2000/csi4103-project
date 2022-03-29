
from PIL import Image, ImageOps

# Takes a file named Image.png and converts it to a greyscale named greyscale.png
# TODO: Make this take in command line arguments.
img = Image.open('../BrachioGraph/images/Image.png').convert('L', dither=None)
img = ImageOps.posterize(img, 2)
img.save('greyscale.png')
