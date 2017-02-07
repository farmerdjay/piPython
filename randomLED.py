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



light = (red, yellow, green, blue, red2, yellow2, green2, blue2)
# yoyo

while True:
    tempColor = random.choice(light)
    tempColor.on()
    #sleep(.05)
    sleep(random.uniform(.01,.03))
    tempColor = random.choice(light)
    tempColor.off()
    #sleep(.05)
    sleep(random.uniform(.01,.03))
