import serial
import RPi.GPIO as GPIO
import time

uno = serial.Serial("/dev/ttyACM1",115200)
        
while True:

        command = (uno.readline()).decode("ASCII")
        print(command)
        if(command == "Y\n"):
                break
        

