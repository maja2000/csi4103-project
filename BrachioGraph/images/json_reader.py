#Code borrowed from https://www.geeksforgeeks.org/read-json-file-using-python/

#This code will read the outputted JSON folder with the lines.
#It will output an array with the appropriate formatting for the Arduino

import json
import os

def read_json(fileName):
    actual_file_name = '/home/pi/csi4103-project/BrachioGraph/images/' + fileName
    print(actual_file_name)
    print(os.getcwd())

    # Opening JSON file
    f = open(fileName)

    # returns JSON object as
    # a dictionary
    data = json.loads(f)

    # Iterating through the json
    # list
    #for i in data['emp_details']:
    #    print(i)

    # Closing file
    f.close()

    print(data)
    return

read_json('africa.jpg.json')