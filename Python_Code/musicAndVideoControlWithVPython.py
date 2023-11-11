# -*- coding: utf-8 -*-
import time
import keyboard
import os
from dotenv import load_dotenv
import serial
from vpython import *

load_dotenv()



data = serial.Serial(os.getenv('PORT'), 9600)
Area = canvas(title="Shahed University")
Area.autoscale = False
Area.width = 1000
Area.height = 600
Area.range = 50
# Ultrasonic sr04 sensor modeling
Board = box(length=20, width=40, height=0.25, color=color.white, pos=vector(-8.5, -2.5, -11.5))

Box2 = box(length=0.25, width=10, height=5, color=color.blue, pos=vector(-0.5, 0, 0))
Trigger2 = cylinder(pos=vector(-0.5, 0, -2.5), color=color.white, length=1.5)
Echo2 = cylinder(pos=vector(-0.5, 0, +2.5), color=color.white, length=1.5)

Box1 = box(length=0.25, width=10, height=5, color=color.blue, pos=vector(-0.5, 0, -25))
Trigger1 = cylinder(pos=vector(-0.5, 0, -27.5), color=color.white, length=1.5)
Echo1 = cylinder(pos=vector(-0.5, 0, -22.5), color=color.white, length=1.5)

are = box(length=15, width=10, height=5, color=color.green, pos=vector(-8, 0, -12.5))
Label = label(pos=vector(-8, 5, -12.5), test="Status : ")
Label.text = "Status : "
# Defining cartesian axis
pointer_x = arrow(pos=vector(0, 0, -11.5), axis=vector(1, 0, 0), color=color.blue)  # x is blue
pointer_y = arrow(pos=vector(0, 0, -11.5), axis=vector(0, 1, 0), color=color.red)  # y is red
pointer_z = arrow(pos=vector(0, 0, -11.5), axis=vector(0, 0, 1), color=color.white)  # z is white

while 1:
    if data.inWaiting() > 0:
        input_data = str(data.readline().decode())
        print(input_data)
        if "Play/Pause" in input_data:
            keyboard.press_and_release('space')
            Label.text = "Status : " + input_data
            Trigger1.color = color.yellow
            Trigger2.color = color.yellow
            Echo1.color = color.yellow
            Echo2.color = color.yellow
            time.sleep(1.5)
            Label.text = "Status : "
            Trigger1.color = color.white
            Trigger2.color = color.white
            Echo1.color = color.white
            Echo2.color = color.white

        elif "Forward" in input_data:
            keyboard.press_and_release('right')
            Label.text = "Status : " + input_data
            Trigger1.color = color.yellow
            Echo1.color = color.yellow
            time.sleep(1.5)
            Label.text = "Status : "
            Trigger1.color = color.white
            Echo1.color = color.white

        elif "Backward" in input_data:
            keyboard.press_and_release('left')
            Label.text = "Status : " + input_data
            Trigger2.color = color.yellow
            Echo2.color = color.yellow
            time.sleep(1.5)
            Label.text = "Status : "
            Trigger2.color = color.white
            Echo2.color = color.white
