import serial
import time

uno = serial.Serial('COM4', 9600)

commands = ['help', 'move', 'grid', 'thumptime', 'frequency', 'two']

print(uno.name)

while True:

	command = raw_input("Command:: ")
	
	if command in commands:
		while True:	
			uno.write(command)
			rx = uno.readline()
			if rx == "two\r\n":
				print("yes")
				break

