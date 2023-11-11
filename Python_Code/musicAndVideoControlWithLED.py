# -*- coding: utf-8 -*-
import keyboard
import os
from dotenv import load_dotenv
import serial


load_dotenv()



data = serial.Serial(os.getenv('PORT'), 9600)
while 1:
    if data.inWaiting() > 0:
        input_data = str(data.readline().decode())
        print(input_data)
        if "Play/Pause" in input_data:
            keyboard.press_and_release('space')

        elif "Forward" in input_data:
            keyboard.press_and_release('right')

        elif "Backward" in input_data:
            keyboard.press_and_release('left')
