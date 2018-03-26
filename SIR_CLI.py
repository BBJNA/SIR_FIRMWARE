import serial
import RPi.GPIO as GPIO
import time
from datetime import datetime

mega = serial.Serial("/dev/ttyACM1",9600)
##mega = serial.Serial('COM4', 9600) ##For windows

print(mega.name)

commands = ['h','x','y','d','t','f','i']

def helpme():
        print("")
        print("h - Display description and syntax of commands")
        print("x - Change X distance")
        print("y - Change Y distance")
        print("t - Number of thumper readings per point")
        print("f- Change the thumper frequency")
        print("i - Get the Gridx, Gridy, Freq of the Arduino")
        print("q - Quit the program")
        print("")

def gridx():
        dist = raw_input("Enter in new X distance: ")
        try:
                int(dist)
        except ValueError:
                print("Incorrect input..")
        else:
                while True:
                        mega.write('x')
                        rx = mega.read(1)
                        if(rx == 'c'):
                                print("Mega Ready")
                                break

                mega.write(dist.encode('ASCII'))
                
                while True:
                        rx = mega.readline()
                        rx = rx[:(len(tx))]
                        if(rx == tx):
                                print("TX Successful")
                                break

def gridy():
        dist = raw_input("Enter in new Y distance: ")
        try:
                int(dist)
        except ValueError:
                print("Incorrect input..")
        else:
                while True:
                        mega.write('y')
                        rx = mega.read(1)
                        if(rx == 'c'):
                                print("Mega Ready")
                                break

                mega.write(dist.encode('ASCII'))
                
                while True:
                        rx = mega.readline()
                        rx = rx[:(len(tx))]
                        if(rx == tx):
                                print("TX Successful")
                                break

def delta():
        dist = raw_input("Enter in new Y distance: ")
        try:
                int(dist)
        except ValueError:
                print("Incorrect input..")
        else:
                while True:
                        mega.write('d')
                        rx = mega.read(1)
                        if(rx == 'c'):
                                print("Mega Ready")
                                break

                mega.write(dist.encode('ASCII'))
                
                while True:
                        rx = mega.readline()
                        rx = rx[:(len(tx))]
                        if(rx == tx):
                                print("TX Successful")
                                break
def info():
        return
##    while True:
##        mega.write(release.encode('ASCII'))
##        rx = mega.readline()
##        print(rx.find("\n"))
##        if rx.find("\n") > 1:
##            mega.write(release.encode('ASCII'))
##            print("Info: " + rx)
##            break
        
while True:
    command = raw_input("Command:: ")
    if command in commands:
        if command == 'x':
                gridx()
        elif command == 'y':
                gridy()
        elif command == 'h':
                helpme()
        elif command == 'i':
                info()
        elif command == 'q':
                break


