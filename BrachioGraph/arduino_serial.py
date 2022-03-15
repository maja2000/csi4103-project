#!/usr/bin/env python3
import serial
import time

def txt_reader(txtName):
    realTxtName ='BrachioGraph/images' + txtName
    with open(txtName) as f:
        data = f.read()
    data += "/n"
    return data

if __name__ == '__main__':
#if False:
    #Need to go through the plaintext_coordinates.txt file and send the coordinates to the Arduino
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    txt_data = txt_reader("/home/pi/csi4103-project/BrachioGraph/images/plaintext_coordinates.txt").encode('utf-8')
    #print(txt_data)
    
    ser.write(txt_data)
    while True:
      line = ser.readline().decode('utf-8').rstrip()
      print(line)
      time.sleep(1)

#txt_reader("/home/pi/csi4103-project/BrachioGraph/images/plaintext_coordinates.txt")
