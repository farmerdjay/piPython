

def main():
    f = open("textfile.txt", "w+")
    for i in range(10):
        f.write("This is line %d\n" % (i+1))
    f.close()

    f = open("textfile.txt", "a+") # appending
    for i in range(10):
        f.write("%d," % (i+1))
    f.close()

    f = open("textfile.txt","r")
    if f.mode == 'r':
        content = f.read()
        print(content)

    f= open("textfile.txt", 'r')
    if f.mode == 'r':
        # readlines read the individual lines into a list
        fl = f.readlines()
        print(fl[2])


if __name__ == "__main__":
    main()
