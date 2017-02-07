from gpiozero import LED
from time import sleep
import random

red = LED(17)
yellow = LED(27)
green = LED(22)
blue = LED(23)
red2 = LED(12)
yellow2 = LED(16)
green2 = LED(20)
blue2 = LED(21)

lightList = (red, yellow, green, blue, red2, yellow2, green2, blue2)

def allOff():
    for element in lightList:
        element.off()


while True:
    allOff()
    sleep(1)
    blue.on()
    blue2.on()
    sleep(1)
    blue.off()
    blue2.off()
    green.on()
    green2.on()
    sleep(1)
    green.off()
    green2.off()
    yellow.on()
    yellow2.on()
    sleep(1)
    yellow.off()
    yellow2.off()
    red.on()
    red2.on()
    sleep(1)

    allOff()
    blue.on()
    blue2.on()
    sleep(1)
    green.on()
    green2.on()
    sleep(1)
    yellow.on()
    yellow2.on()
    sleep(1)
    red.on()
    red2.on()
    sleep(1)
    
    green.on()
    sleep(1)
    green.off()
    
    
