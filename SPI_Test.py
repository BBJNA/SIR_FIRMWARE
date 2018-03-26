import spidev
import time
import RPi.GPIO as gpio
from datetime import datetime

i = 0
sample = 0
site = 0
dataWriteBuffer = []
fileWriteCounter = 0

A = 31
B = 33
C = 35
CONVST = 37

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(CONVST, gpio.OUT)
gpio.setup(A, gpio.OUT)
gpio.setup(B, gpio.OUT)
gpio.setup(C, gpio.OUT)
gpio.output(A,0)
gpio.output(B,0)
gpio.output(C,0)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 3900000

def WaitCommand():
    return    

def TestInit():
    fileName = str(datetime.now()).split()
    fileName[1] = fileName[1].split('.')
    fileName = str(fileName[0]+"@"+fileName[1][0]+"_"+fileName[1][1])
    return fileName

def AdcChannelRead(channel):
    
    gpio.output(A,((channel)&0x01))
    gpio.output(B,((channel>>1)&0x01))
    gpio.output(C,((channel>>2)&0x01))
    
    data = spi.xfer2([0x00,0x00,0x00,0x00,0x00,0x00])
    return str(str((data[0]<<8)+data[1]).zfill(5)+","+str((data[2]<<8)+data[3]).zfill(5)+","+str((data[4]<<8)+data[5]).zfill(5))

dataFile = open(TestInit(), "w")
start = datetime.now()
site = 2500
while site < 2501:
    
    WaitCommand()
    sampleStartTime = str(datetime.now()).split()
    
    while sample < 1001:
        gpio.output(CONVST,True)
        dataWriteBuffer.append(AdcChannelRead(0))
        dataWriteBuffer.append(AdcChannelRead(1))
        dataWriteBuffer.append(AdcChannelRead(2))
        dataWriteBuffer.append(AdcChannelRead(3))
        dataWriteBuffer.append(AdcChannelRead(4))
        dataWriteBuffer.append(AdcChannelRead(5))
        gpio.output(CONVST,False)
        sample += 1

    sampleStopTime = str(datetime.now()).split()

    dataFile.write("Site" + str(site).zfill(4) + "," + sampleStartTime[1] + "\r\n")    

    for x in dataWriteBuffer:
        dataFile.write(x)
        if fileWriteCounter < 5:
            dataFile.write(',')
            fileWriteCounter += 1

        else:
            fileWriteCounter = 0
            dataFile.write('\n')
    
    dataFile.write("Site" + str(site).zfill(4) + "," + sampleStopTime[1] + "\r\n")

    dataWriteBuffer = []
    sample = 0
    site += 1
    
end = datetime.now()
dataFile.close()
print (start)
print (end)
