from gpiozero import LED
from time import sleep
import random
import pygame.mixer
from pygame.mixer import Sound

red = LED(17)
yellow = LED(27)
green = LED(22)
blue = LED(23)
red2 = LED(12)
yellow2 = LED(16)
green2 = LED(20)
blue2 = LED(21)

numberOfCorrect = 0
numberOfIncorrect = 0

#===============================================#
#   Light Control           ====================#
#===============================================#
def lightShow():
    allLightsOff()
    sleep(.3)
    lightRun()
    lightRunBackward()
    allLightsOn()
    sleep(.2)
    allLightsOff()
    sleep(.2)
    allLightsOn()
    sleep(.2)
    allLightsOff()
    sleep(.3)
    allLightsOn()
    sleep(.3)
    allLightsOff()

def lightRun():
    allLightsOff()
    for i in allLights():
        i.on()
        sleep(.1)
        i.off()

def lightRunBackward():
    allLightsOff()
    for i in reversed(allLights()):
        i.on()
        sleep(.1)
        i.off()

def allLights():
    lights = red, yellow, green, blue, blue2, green2, yellow2, red2
    return lights

def allLightsOff():
    for i in allLights():
        i.off()

def allLightsOn():
    for i in allLights():
        i.on()

def lightUp(color):
    for i in xrange(5):
            color.on()
            sleep(.1)
            color.off()
            sleep(.1)
    return

def answerLight(value):
    global numberOfCorrect
    global numberOfIncorrect

    num = numberOfCorrect - numberOfIncorrect
    if num < 0:
        num = 0
    if num > len(allLights()):
        num = len(allLights())
        if value == True:
            lightShow()
    allLightsOff()
    for i in xrange(num):
        allLights()[i].on()
    return

# Light Related End ========================#


def askAdd(num1, num2):
    print num1, "+", num2, "=",
    input = getNumberInput()
    return input

def checkAdd(num1, num2, input):
    return input != num1 + num2

def askRange():
    print "Please enter the minimum number: ",
    min = int(raw_input())
    print "Please enter the maximum number: ",
    max = int(raw_input())
    print ""
    return min, max

def answerSound(bvalue):
    if bvalue:
        Sound("soundSamples/aRight" + str(random.choice(range(7))) + ".wav").play()
    else:
        Sound("soundSamples/aWrong" + str(random.choice(range(7))) + ".wav").play()

def answerResponse(bvalue):
    global numberOfCorrect
    global numberOfIncorrect
    if bvalue:
        numberOfCorrect += 1
        answerSound(True)
        answerLight(True)
    else:
        numberOfIncorrect += 1
        answerSound(False)
        answerLight(False)

def addition(num1, num2):
    input = askAdd(num1, num2)
    if input == None:
        return False

    while checkAdd(num1, num2, input):
        answerResponse(False)
        input = askAdd(num1, num2)
    answerResponse(True)
    return

def additionGame():
    min, max = askRange()

    while True:
        num1 = random.randint(min, max)
        num2 = random.randint(min, max)

        if addition(num1, num2) == False:
            # Quiting
            print "---------------------------------------"
            break
        print ""
    return

def askSubtract(num1, num2):
    print num1, "-", num2, "=",
    input = getNumberInput()
    return input

def checkSubtract(num1, num2, input):
    return input != num1 - num2

def subtraction(num1, num2):
    input = askSubtract(num1, num2)
    if input == None:
        return False

    while checkSubtract(num1, num2, input):
        answerResponse(False)
        input = askSubtract(num1, num2)
    answerResponse(True)
    return

def subtractionGame():
    max = askMax()

    while True:
        num1 = random.randint(1, max)
        num2 = random.randint(1, num1)

        if subtraction(num1, num2) == False:
            # Quiting
            print "---------------------------------------"
            break
        print ""
    return

def askMultiplication(num1, num2):
    print num1, "x", num2, "=",
    input = getNumberInput()
    return input

def checkMultiplication(num1, num2, input):
    return input != num1 * num2

def multiplication(num1, num2):
    input = askMultiplication(num1, num2)
    if input == None:
        return False

    while checkMultiplication(num1, num2, input):
        answerResponse(False)
        input = askMultiplication(num1, num2)
    answerResponse(True)
    return

def multiplicationGame():
    while True:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        if multiplication(num1, num2) == False:
            # Quiting
            print "---------------------------------------"
            break
        print ""
    return

def askMax():
    print "Please enter the maximum number: ",
    max = int(raw_input())
    print ""
    return max

def askAddingMissing(num1, num2):
    print num1, "+ __ =", num2, "?",
    input = int(raw_input())
    return input

def checkAddingMissing(num1, num2, input):
    return num1 + input != num2

def addingMissing(num1, num2):
    input = askAddingMissing(num1, num2)

    while checkAddingMissing(num1, num2, input):
        answerResponse(False)
        input = askAddingMissing(num1, num2)
    answerResponse(True)
    print "Yes!", num1, "+", input, "=", num2
    return

def addingMissingGame():
    max = askMax()

    while True:
        num1 = random.randint(1, max)
        num2 = random.randint(num1, max)

        addingMissing(num1, num2)
        print ""
    return

def getNumberOfCorrect():
    global numberOfCorrect
    return numberOfCorrect

def getNumberOfIncorrect():
    global numberOfIncorrect
   :echo has('python') || has('python3') return numberOfIncorrect

def printResult():
    print ""
    print "Number of Correct:", getNumberOfCorrect()
    print "Number of Incorrect:", getNumberOfIncorrect()
    if getNumberOfCorrect() + getNumberOfIncorrect() != 0:
        sum = getNumberOfCorrect() + getNumberOfIncorrect()
        print "Grade:", getNumberOfCorrect()*100.0/sum
    else:
        print "Grade: 000"
    print ""

def getNumberInput():
    temp = raw_input()
    while True:
        if temp.isdigit():
            return int(temp)
        if temp == "q":
            printResult()
            return
        print "That is non-sense. Try again (Enter q to quit): "
        temp = raw_input()

def printTitle():
    print "**********************************"
    print "|            Welcome to          |"
    print "|                the             |"
    print "|            MATH GAMES          |"
    print "**********************************"
    print ""

def chooseGame():
    print "Which game would you like to play?"
    print "1) Addition"
    print "2) Adding Missing"
    print "3) Subtraction"
    print "4) Multiplication"
    print ""
    print "Enter a number:",
    return int(raw_input())

while True:
    printTitle()

    pygame.mixer.init()

    while True:
        game = chooseGame()
        print""

        if game == 1:
            additionGame()
        elif game == 2:
            addingMissingGame()
        elif game == 3:
            subtractionGame()
        elif game == 4:
            multiplicationGame()

