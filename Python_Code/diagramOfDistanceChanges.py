import serial
import os
from dotenv import load_dotenv
from vpython import *
from drawnow import *
import matplotlib.pyplot as plt

load_dotenv()
distances = []
num = 0
plt.ion()


def Figure():
    plt.ylim(2, 40)
    plt.title('Ultrasonic live diagram')
    plt.grid(True)
    plt.ylabel('Disance in cm')
    plt.plot(distances, 'ro-', label='Distance Data')
    plt.legend(loc='upper right')


data = serial.Serial(os.getenv('PORT'), 9600)

while 1:
    rate(5)
    if data.inWaiting() > 0:
        distances.append(round(float(data.readline().decode())))
        drawnow(Figure)
        num += 1
        if num > 30:
            distances.pop(0)
