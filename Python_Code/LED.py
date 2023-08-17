import serial
import os
from dotenv import load_dotenv
import time

load_dotenv()
data = serial.Serial(os.getenv('PORT'), 9600)
print(data.readline().decode())
while 1:
    var = int(input("Enter 0 or 1 : "))
    if var == 1:
        data.write('1'.encode())
        print("LED is ON")
        time.sleep(1)
    elif var == 0:
        data.write('0'.encode())
        print("LED is OFF")
        time.sleep(1)
    else:
        print("END")
        exit(0)
