#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    #Need to go through the JSON file and send the lines to the Arduino

    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        ser.write(b"Hello from Raspberry Pi!\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
