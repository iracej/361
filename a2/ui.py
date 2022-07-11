from time import sleep


def main():
    userIn = input("Want some pictures? (y/n)\n")
    if userIn == 'y':
        prngFile = open("prng-service.txt", "w")
        prngFile.write("run")
        prngFile.close()
        sleep(12)
        prngFile = open("prng-service.txt", "r")
        prngResult = prngFile.read()
        prngFile.close()
        imgFile = open("image-service.txt", "a")
        imgFile.write(prngResult)
        imgFile.close()
        sleep(12)
        imgFile = open("image-service.txt", "r")
        imgPath = imgFile.read()
        imgFile.close()
        print("Here is your picture: ", imgPath)

    elif userIn == 'n':
        print("goodbye then\n")
    else:
        print("Methink’st thou art a general offence and every man should beat thee.\n")

main()
