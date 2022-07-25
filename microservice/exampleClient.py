import rpyc

c = rpyc.connect("localhost", 22122)
userInput = input("Enter your password.\n")
correct = c.root.validatePassword(userInput)
if correct:
    print("Correct.")
    changePW = input("Want to change your password? (y/n)\n")
    if changePW == "y":
        changePW = input("Input your new password.\n")
        c.root.validatePassword(userInput, changePW)
else:
    print("Incorrect.")