import serial
import os
from dotenv import load_dotenv
from vpython import *

load_dotenv()

Area = canvas(title="Shahed University")
Area.autoscale = False
Area.width = 1000
Area.height = 600
Area.range = 50
data = serial.Serial(os.getenv('PORT'), 9600)
ruler = cylinder(pos=vector(0, 0, 0), color=vector(1, 0, 0))
Label = label(pos=vector(0, 4, 0), test="Hello")
while 1:
    rate(20)
    if data.inWaiting() > 0:
        print(round(float(data.readline().decode())))
        ruler.length = round(float(data.readline().decode()))
        Label.text = "Hello : " + str(round(float(data.readline().decode())))

