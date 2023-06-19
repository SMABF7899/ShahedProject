import serial
import time

ArduinoData = serial.Serial('/dev/cu.usbmodem12101', 9600)
print(ArduinoData.readline().decode())
while True:
    var = input("Enter zero or one : ")
    if var == '1':
        ArduinoData.write('1'.encode())
        print("LED is On")
        time.sleep(1)
    elif var == '0':
        ArduinoData.write('0'.encode())
        print("LED is OFF")
        time.sleep(1)
    elif var == "exit":
        exit(0)
    else:
        print("Error: The number must be 0 or 1")
        time.sleep(1)
