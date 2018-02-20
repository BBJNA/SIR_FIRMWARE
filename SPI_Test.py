import spidev
import time
import RPi.GPIO as gpio

sample = 0

A=36
B=38
C=40
CONVST = 37

gpio.setmode(gpio.BOARD)
gpio.setup(CONVST, gpio.OUT)
gpio.setup(A, gpio.OUT)
gpio.setup(B, gpio.OUT)
gpio.setup(C, gpio.OUT)
gpio.output(A,0)
gpio.output(B,0)
gpio.output(C,0)

spi = spidev.SpiDev()
spi.open(0,0)

i=0
def AdcChannelRead(channel):
    print('Channel ' + str(channel))
    gpio.output(A,((channel)&0x01))
    gpio.output(B,((channel>>1)&0x01))
    gpio.output(C,((channel>>2)&0x01))
    print(format((channel&0x01), '02x')),
    print(format(((channel>>1)&0x01), '02x')),
    print(format(((channel>>2)&0x01), '02x')),

    
    data = spi.xfer2([0x00,0x00,0x00,0x00,0x00,0x00])

    for index, val in enumerate(data):
        print(format(val, '02x')),
    print('')

while sample < 50:
    gpio.output(CONVST,True)
    AdcChannelRead(0)
    time.sleep(1)
    AdcChannelRead(1)
    time.sleep(.5)
    gpio.output(CONVST,False)
    time.sleep(.5)
    sample = 50
