import serial
import keyboard
import time

data = serial.Serial('/dev/cu.usbmodem12101', 9600)

while 1:
    if data.inWaiting() > 0:
        input_data = data.readline()
        print(input_data)
        input_data = str(input_data)
        if "Play/Pause" in input_data:
            keyboard.press_and_release('space')
            time.sleep(2)
        elif "Forward" in input_data:
            keyboard.press_and_release('right')
            time.sleep(2)
        elif "Backward" in input_data:
            keyboard.press_and_release('left')
            time.sleep(2)
