import serial
import RPi.GPIO as GPIO
import time
from datetime import datetime

mega = serial.Serial("/dev/ttyACM2",9600)
print(mega.name)

while True:
        
        command = raw_input("Command:: ")
        while True:
                mega.write(command.encode('ASCII'))
                rx = mega.read(1)
                if(rx == 'c'):
                        print("\n\nMega Ready")
                        break

        tx = raw_input("Y Value: ")        
        mega.write(tx.encode('ASCII'))
        
        while True:
                rx = mega.readline()
                rx = rx[:(len(tx))]
                if(rx == tx):
                        print("\n\nTX Successful")
                        break

