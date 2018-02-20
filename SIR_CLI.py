import serial
import RPi.GPIO as GPIO
import time

uno = serial.Serial("/dev/ttyACM1",9600)
##uno = serial.Serial('COM4', 9600) ##For windows

print(uno.name)

commands = ['help', 'move', 'gridx', 'gridy', 'thumps', 'freq' ,'start', 'info']
release = "check"

def helpme():
        print("")
        print("help - Display description and syntax of commands")
        print("move - Manual movement on")
        print("gridx - Change X distance")
        print("gridy - Change Y distance")
        print("thumps - Number of thumper readings per point")
        print("freq - Change the thumper frequency")
        print("start - Start the testing protocol")
        print("info - Get the Gridx, Gridy, Freq of the Arduino")
        print("")

def gridx():
        dist = raw_input("Enter in new X distance: ")
        try:
                int(dist)
        except ValueError:
                print("Incorrect input..")
        else:
                uno.write(dist.encode('ASCII'))
                while True:
                        rx = uno.readline()
                        if rx == 'Y\n':
                            uno.write(release.encode('ASCII'))
                            print("Gridx = " + dist)
                            break
def gridy():
        dist = raw_input("Enter in new Y distance: ")
        try:
                int(dist)
        except ValueError:
                print("Incorrect input..")
        else:
                uno.write(dist.encode('ASCII'))
                while True:
                        rx = uno.readline()
                        if rx == 'Y\n':
                            uno.write(release.encode('ASCII'))
                            print("Gridy = " + dist)
                            break
def info():
    while True:
        uno.write(release.encode('ASCII'))
        rx = uno.readline()
        print(rx.find("\n"))
        if rx.find("\n") > 1:
            uno.write(release.encode('ASCII'))
            print("Info: " + rx)
            break
        
while True:

        command = raw_input("Command:: ")
        if command in commands:
            if command == 'gridx':
                    uno.write(command.encode('ASCII'))
                    gridx()
            elif command == 'gridy':
                    uno.write(command.encode('ASCII'))
                    gridy()
            elif command == 'help':
                    helpme()
            elif command == 'info':
                    uno.write(command.encode('ASCII'))
                    info()


