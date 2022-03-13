#Code borrowed from https://www.geeksforgeeks.org/read-json-file-using-python/

#This code will read the outputted JSON folder with the lines.
#It will output an array with the appropriate formatting for the Arduino

import json

def read_json(fileName):
    line_array = array[]

    # Opening JSON file
    f = open(fileName)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    #for i in data['emp_details']:
    #    print(i)

    # Closing file
    f.close()

    print(data)
    return

read_json('africa.jpg.json')