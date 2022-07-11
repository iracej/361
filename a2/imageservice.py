from time import sleep
from os.path import exists


def main():
    keepGoing = True
    imgFile = open("image-service.txt", "r")
    while keepGoing:
        fileContents = imgFile.read()
        if fileContents != "":
            # write file path to file thingy
            print("File contains image ID!\n")
            sleep(10)
            imageID = "./"
            imageID += fileContents
            imageID += ".jpg"
            imgFile.close()
            imgFile = open("image-service.txt", "w")
            imgFile.write(imageID)
            print("Wrote ", imageID, " to file\n")
            keepGoing = False
            imgFile.close()
            sleep(20)   # give ui plenty of time to fetch imageID
            open("image-service.txt", "w").close()
            print("Deleted contents of image-service.txt\n")
        else:
            print("File does not contain image ID. Waiting...\n")
            sleep(1)


main()
