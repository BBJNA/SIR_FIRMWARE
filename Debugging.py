import spidev
import time
import RPi.GPIO as gpio
from datetime import datetime

i = 0
sample = 0
site = 0

A=31
B=33
C=35
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

def AdcChannelRead(channel):

    gpio.output(A,((channel)&0x01))
    gpio.output(B,((channel>>1)&0x01))
    gpio.output(C,((channel>>2)&0x01))
    data = spi.xfer2([0x00,0x00,0x00,0x00,0x00,0x00])
    z = (data[0]<<8)+data[1]
    y = (data[2]<<8)+data[3]
    x = (data[4]<<8)+data[5]
    #print ("Channel: " + str(channel))
    print (str(z) + "," + str(y) + "," + str(x))
    
    return data
    
while site < 2500:

    while sample < 2:

        gpio.output(CONVST,True)

        AdcChannelRead(5)
        time.sleep(1)

        AdcChannelRead(4)
        time.sleep(1)
        
        AdcChannelRead(3)
        time.sleep(1)

        AdcChannelRead(2)
        time.sleep(1)

        AdcChannelRead(1)
        time.sleep(1)

        AdcChannelRead(0)
        time.sleep(1)
        
        gpio.output(CONVST,False)
        sample += 1
        #time.sleep(01)
    sample = 0
    site = 2500

