import spidev
import time
import RPi.GPIO as gpio
from datetime import datetime

i = 0
sample = 0
site = 0

A=36
B=38
C=40
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
spi.max_speed_hz = 488000

def TestInit():
    fileName = str(datetime.now()).split()
    fileName[1] = fileName[1].split('.')
    fileName = str(fileName[0]+"@"+fileName[1][0]+"_"+fileName[1][1])
    return fileName

def AdcChannelRead(channel):
    #print('Channel ' + str(channel))
    gpio.output(A,((channel)&0x01))
    gpio.output(B,((channel>>1)&0x01))
    gpio.output(C,((channel>>2)&0x01))
##    print(format((channel&0x01), '02x')),
##    print(format(((channel>>1)&0x01), '02x')),
##    print(format(((channel>>2)&0x01), '02x')),
    
    data = spi.xfer2([0x00,0x00,0x00,0x00,0x00,0x00])
    dataFile.write(str((data[0]<<8)+data[1]).zfill(5)+","+str((data[2]<<8)+data[3]).zfill(5)+","+str((data[4]<<8)+data[5]).zfill(5)+" ")

def getSiteConfig():

    configFile = open("SIR.config","r")
    xPlotMax = configFile.readline()
    yPlotMax = configFile.readline()
    Frequency = configFile.readline()

    try:
        xPlotMax = int(xPlotMax)
        yPlotMax = int(yPlotMax)
        Frequency = int(Frequency)
    except Exception as e:
        print(str(e) + " is not a number..Check SIR.config")

    configFile.close()
    return [xPlotMax, yPlotMax, Frequency]
    

siteConf = getSiteConfig()
dataFile = open(TestInit(), "w")
start = datetime.now()

while site < 2500:

    sampleTime = str(datetime.now()).split()
    dataFile.write("Site" + str(site).zfill(4) + "," + sampleTime[1] + "\r\n")    

    while sample < 10000:
        gpio.output(CONVST,True)
        AdcChannelRead(0)
        #AdcChannelRead(1)
        #AdcChannelRead(2)
        #AdcChannelRead(3)
        #AdcChannelRead(4)
        #AdcChannelRead(5)
        dataFile.write("\r\n")
        gpio.output(CONVST,False)
        sample += 1

    sampleTime = str(datetime.now()).split()
    dataFile.write("Site" + str(site).zfill(4) + "," + sampleTime[1] + "\r\n")
    
    sample = 0
    site = 2500

end = datetime.now()
dataFile.close()
print start
print end
