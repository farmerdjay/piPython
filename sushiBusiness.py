from gpiozero import LED
from gpiozero import Button
from time import sleep
from datetime import datetime
from os.path import expanduser
expanduser("~")

red = LED(17)
yellow = LED(27)
green = LED(22)
blue = LED(23)
red2 = LED(12)
yellow2 = LED(16)
green2 = LED(20)
blue2 = LED(21)

button = Button(4)

lights = [red, yellow, green, blue, blue2, green2, yellow2, red2]
count = 0

def lightsOn():
	for color in lights:
		color.on()
		
def lightsOff():
	for color in lights:
		color.off()

def lightsBlink():
	lightsOff()
	sleep(.3)
	lightsOn()
	sleep(.3)
	lightsOff()

def lightsBlinkTimes(number):
	for i in range(number):
		lightsBlink()
	
def whenButtonPressed():
	global count
	
	red2.on()
	sleep(.8)
	
	lights[count].on()
	#print(datetime.now())
	#print(button.held_time)
	
	if count < 7:
		count = count + 1

def writeSushiLog(string):
	with open(expanduser("~")+'/Desktop/sushi.log', 'a') as f:
		f.write(string+'\n')

def main():
	
	while True:

		global count
		
		button.wait_for_press()
		count = 0
		
		while button.is_pressed:
			whenButtonPressed()

		if count - 1 ==  1:
			writeSushiLog(str(datetime.now())[:19]+'\tpee')
		elif count - 1 == 2:
			writeSushiLog(str(datetime.now())[:19]+'\tpoop')
		elif count - 1 == 3:
			writeSushiLog(str(datetime.now())[:19]+'\teat')
		else:
			lightsBlinkTimes(3)
		
		button.wait_for_release()
		lightsOff()
		
main()
    


