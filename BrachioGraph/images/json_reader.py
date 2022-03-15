# Code borrowed from https://www.geeksforgeeks.org/read-json-file-using-python/
# Can be run with arguments, or by changing the call statement at the bottom

# This code will read the outputted JSON folder with the lines. It will output a 3D array with coordinates for the
# bracchiograph Ex. Output below: [[[2, 0], [2, 16], [2, 32], [2, 48], [2, 64], [2, 80], [2, 96], [2, 112], [2, 128],
# [2, 144], [2, 160], [2, 176], [2, 192], [2, 208], [2, 224], [2, 240], [2, 256], [2, 272], [2, 288], [2, 304], [2,
# 320], [2, 336], [2, 352], [2, 368], [2, 384], [2, 400], [2,


import json
import os


# The function TODO
def read_json(fileName):
    # Correct the file path, just in case
    actual_file_name = '/home/pi/csi4103-project/BrachioGraph/images/' + fileName
    # print(actual_file_name)
    # print(os.getcwd())

    # Opening JSON file
    f = open(fileName)

    # returns JSON object as
    # a dictionary
    data = json.loads(f.read())

    # Iterating through the json
    # list
    # for i in data['emp_details']:
    #    print(i)

    # Closing file
    f.close()

    print(data)
    return data


def write_to_text(jsonData):
    with open('plaintext_coordinates.txt', 'w') as f:
        for item in jsonData:
            f.write(str(item))
        return


json_data = read_json("africa.jpg.json")
write_to_text(json_data)
