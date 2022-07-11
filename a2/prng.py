import random
from time import sleep


def main():
    keepGoing = True
    prngFile = open("prng-service.txt", "r")
    while keepGoing:
        fileContents = prngFile.read()
        if fileContents == "run":
            print("File contains run command!\n")
            sleep(10)
            output = random.randint(1, 5)
            prngFile.close()
            prngFile = open("prng-service.txt", "w")
            prngFile.write(str(output))
            prngFile.close()
            print("Wrote ", output, " to file\n")
            keepGoing = False
            sleep(20)
            open("prng-service.txt", "w").close()
            print("Deleted contents of prng-service.txt\n")
        else:
            print("File does not contain run command. Waiting...\n")
            sleep(1)


main()
