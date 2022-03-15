import os

exec(open('image_processing.py').read())

cwd = os.getcwd()
os.chdir(cwd + "/images")
cwd = os.getcwd()

exec(open('json_reader.py').read())
