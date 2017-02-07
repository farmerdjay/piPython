from gpiozero import LED
from time import sleep

red = LED(17)
yellow = LED(27)
green = LED(22)
blue = LED(23)
red2 = LED(12)
yellow2 = LED(16)
green2 = LED(20)
blue2 = LED(21)

light = (red, yellow, green, blue, blue2, green2, yellow2, red2)

def flash(light, second):
    light.on()
    sleep(second)
    light.off()

while True:
    for i in light:
        flash(i,.15)

    for i in reversed(light[1:len(light)-1]):
        flash(i,.15)

