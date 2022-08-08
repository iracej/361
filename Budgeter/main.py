import datetime

# to do:
# consider making functions into class functions
# write display function
# write function to store Transaction object in file
# write function to read several Transaction objects from a file


class Transaction:
    def __init__(self):
        self.amount = None
        self.date = None
        self.category = None
        self.notes = None

    def getAmount(self):
        print("How much money was the transaction?")
        print("(Enter a number, negatives are allowed)")
        amount = input()
        i = True
        while i:
            try:
                amount = float(amount)
                i = False
            except ValueError:
                print("That isn't a number. Please enter a different value.")
                amount = input()
        self.amount = amount

    def getDate(self):
        print("When did the transaction occur?")
        print("(Enter in MM/DD/YYYY format)")
        i = True
        while i:
            date = input()
            if len(date) == 10:
                if date[2] == '/' and date[5] == '/':
                    i = False
                    self.date = date
                else:
                    print("That's not a valid date! Please try again.")
            else:
                print("That's not a valid date! Please try again.")

    def getCategory(self):
        print("What category does the transaction belong to?")
        i = True
        while i:
            category = input()
            if len(category) > 0:
                i = False
                self.category = category
            else:
                print("That's not a valid date! Please try again.")

    def getNotes(self):
        print("Would you like to enter any notes?")
        print("(Enter your notes here, or leave it blank)")
        notes = input()
        if len(notes) == 0:
            self.notes = None
        else:
            self.notes = notes

    def getData(self):
        print("You are about to create a new transaction record,")
        print("which will include the amount, date, category, and any notes.")
        keepGoing = input("Would you like to continue? (Y/N)\n")
        if keepGoing == 'Y' or keepGoing == 'y':
            self.getAmount()
            self.getDate()
            self.getNotes()
        else:
            print("Cancelling input.")

    def confirm(self):
        print("You entered the following:")
        print("Amount: ", self.amount)
        print("Date: ", self.date)
        print("Notes: ", self.notes)
        print("Is that correct? (Y/N)")
        correctness = input()
        if correctness == 'Y' or correctness == 'y':
            return True
        else:
            return False


def main():
    keepGoing = True
    print("Welcome to version 0.0.2 of the Budgeter!")
    while keepGoing:
        print("What would you like to do? (Enter a letter)")
        print("A. Enter a new transaction into your record")
        print("B. View the contents of your record")
        print("C. Edit/delete an entry in your record")
        print("D. Close the program")
        whatToDo = input()
        if whatToDo == 'A' or whatToDo == 'a':
            currentTransaction = Transaction()
            currentTransaction.getData()
            doWeSave = currentTransaction.confirm()
            del currentTransaction  # eventually replace with write function
        elif whatToDo == 'B' or whatToDo == 'b':
            print("Not yet implemented. Sorry.")
        elif whatToDo == 'C' or whatToDo == 'c':
            print("Not yet implemented. Sorry.")
        elif whatToDo == 'D' or whatToDo == 'd':
            print("Thank you for using the Budgeter. Goodbye.")
            keepGoing = False
        else:
            print("That doesn't seem to be a valid option. Please try again.")


main()
