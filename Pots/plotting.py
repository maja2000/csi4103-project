import numpy
import pandas as pd
import math

# reading the excel sheet, in this instance it is the box pot measurements
file_name = "../NicksScrewingAround/Validation/boxPotMeasurements.xlsx"
df = pd.read_excel(file_name, sheet_name="Sheet1")

samplePeriod = (df['time']).diff().mean()

vtheta1 = df['Vtheta1']
vtheta2 = df['Vtheta2']
vt1_0 = vtheta1[0:int(100e-3/samplePeriod)].mean()
vt2_0 = vtheta2[0:int(100e-3/samplePeriod)].mean()
t1_0Actual = 180 #degrees
t2_0Actual = 100 #degrees

# Find starting point of Vt1
prevVal = df["Vtheta1"].iloc[1]
for k in range(1, len(df['time'])):
    currentVal = df["Vtheta1"].iloc[k]
    if currentVal - prevVal >= 0.05:
        break

# Find starting point of Vt2
prevVal = df["Vtheta2"].iloc[1]
for m in range(1, len(df['time'])):
    currentVal = df["Vtheta1"].iloc[k]
    if currentVal - prevVal >= 0.05:
        break

# Find which one starts first
n = min(k,m)
startIdx = n - 200e-3/samplePeriod # Back off start idx by 200 ms

# Find ending point of Vt1
prevVal = df["Vtheta1"].iloc[-1]
for p in range(len(df['time'])-1, 0, -1):
    currentVal = df["Vtheta1"].iloc[p]
    if currentVal - prevVal >= 0.05:
        break

# Find ending point of Vt2
prevVal = df["Vtheta2"].iloc[-1]
for q in range(len(df['time'])-1, 0, -1):
    currentVal = df["Vtheta1"].iloc[p]
    if currentVal - prevVal >= 0.05:
        break

# Find which one ends last
n = max(p,q)
endIdx = n + 200e-3/samplePeriod #Back off start idx by 200 ms

# Trimming off the garbage
Vt1 = df["Vtheta1"].iloc[int(startIdx):int(endIdx)]
Vt2 = df["Vtheta2"].iloc[int(startIdx):int(endIdx)]
t = df["time"].iloc[int(startIdx):int(endIdx)]

# Convert Voltage to degrees
minVoltage = 0
maxVoltage = 5
minAngle = 0
maxAngle = 270

slope = (maxAngle - minAngle)/(maxVoltage - minVoltage)

t1_0 = -slope*vt1_0 + maxAngle
t2_0 = -slope*vt2_0 + maxAngle

t1 = slope*Vt1 + maxAngle - 180
t2 = -slope*Vt2 + 250


# Convert Theta to XY
R1 = 11
R2 = 10.4
t3 = t1 + t2 - 180

v1x = R1*numpy.cos(t1*math.pi/180)
v1y = R1*numpy.sin(t1*math.pi/180)
v1 = pd.concat([v1x,v1y], axis=1)


v2x = R2*numpy.cos(t3*math.pi/180)
v2y = R2*numpy.sin(t3*math.pi/180)
v2 = pd.concat([v2x,v2y], axis=1)
