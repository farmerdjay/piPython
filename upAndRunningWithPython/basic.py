f = 33

def main2():
    global f
    print(f)
    f = 0
    print(f)

def addMulti(*args):
    result = 0
    for i in args:
        result = result + i
    return result

def ifstatement():
    x = 10
    y = 20

    if (x < y):
        print("x < y")
    elif (x == y):
        print("x = y")
    else:
        print("x > y")

def whileloop():
    x = 0

    while (x < 5):
        print(x)
        x = x + 1

def forloop():
    for x in range(0,8):
        if (x == 5):
            break
        if (x % 2 == 0):
            print("It is even.")
            continue
        print(x)

    data = [23, "food", f]
    for x in data:
        print(x)

    for i, d in enumerate(data):
        print(i, d)

class animal():
    def move(self):
        print("animal can  move")

    def jump(self, someString):
        print("animal can jump and: " + someString)

class dog(animal):
    def bark(self):
        print("dog can bark")

    def move(self):
        animal.move(self)
        print("dog can move")


if __name__ == "__main__":
    main2()
    print(addMulti(1,1,2,3,5))
    ifstatement()
    whileloop()
    forloop()
    
    a = animal()
    a.move()
    a.jump("see")

    d = dog()
    d.move()



