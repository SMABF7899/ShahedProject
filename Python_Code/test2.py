import time

import serial
from vpython import *
import time

# Ultrasonic sr04 sensor modeling
Board = box(length=20, width=40, height=0.25, color=color.white, pos=vector(-8.5, -2.5, -11.5))

Box1 = box(length=0.25, width=10, height=5, color=color.blue, pos=vector(-0.5, 0, 0))
Trigger1 = cylinder(pos=vector(-0.5, 0, -2.5), color=color.white, length=1.5)
Echo1 = cylinder(pos=vector(-0.5, 0, +2.5), color=color.white, length=1.5)

Box2 = box(length=0.25, width=10, height=5, color=color.blue, pos=vector(-0.5, 0, -25))
Trigger2 = cylinder(pos=vector(-0.5, 0, -27.5), color=color.white, length=1.5)
Echo2 = cylinder(pos=vector(-0.5, 0, -22.5), color=color.white, length=1.5)

are = box(length=15, width=10, height=5, color=color.green, pos=vector(-8, 0, -12.5))
# Defining cartesian axis
pointer_x = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), color=color.blue)  # x is blue
pointer_y = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.red)  # y is red
pointer_z = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), color=color.white)  # z is white

time.sleep(5)
data = "Forward"

if "Play/Pause" in data:
    print(data)
    Trigger1.color = color.yellow
    Trigger2.color = color.yellow
    Echo1.color = color.yellow
    Echo2.color = color.yellow
    time.sleep(1.5)
    Trigger1.color = color.white
    Trigger2.color = color.white
    Echo1.color = color.white
    Echo2.color = color.white


elif "Forward" in data:
    print(data)
    Trigger2.color = color.yellow
    Echo2.color = color.yellow
    time.sleep(1.5)
    Trigger2.color = color.white
    Echo2.color = color.white

elif "Backward" in data:
    print(data)
    Trigger1.color = color.yellow
    Echo1.color = color.yellow
    time.sleep(1.5)
    Trigger1.color = color.white
    Echo1.color = color.white

# while 1 == 1:
#     rate(25)
#     SensorColor = "1,0,0"
#     ColorNumbers = SensorColor.split(',')
#     red = float(ColorNumbers[0])
#     green = float(ColorNumbers[1])
#     blue = float(ColorNumbers[2])
#
#     if red < blue and red < green and red <= 20:
#         Plane.color = (1, 0, 0)
#     elif blue < red and blue < green:
#         Plane.color = (0, 0, 1)
#     elif green < red and green < blue:
#         Plane.color = (0, 1, 0)
