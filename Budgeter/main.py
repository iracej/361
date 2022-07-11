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
        self.notes = None


def getAmount():
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
    return amount


def getDate():
    print("When did the transaction occur?")
    print("(Enter in MM/DD/YYYY format)")
    i = True
    while i:
        date = input()
        if len(date) == 10:
            if date[2] == '/' and date[5] == '/':
                i = False
                return date
            else:
                print("That's not a valid date! Please try again.")
        else:
            print("That's not a valid date! Please try again.")


def getNotes():
    print("Would you like to enter any notes?")
    print("(Enter your notes here, or leave it blank)")
    notes = input()
    if len(notes) == 0:
        return None
    else:
        return notes


def main():
    currentTransaction = Transaction()
    currentTransaction.amount = getAmount()
    print(currentTransaction.amount)
    currentTransaction.date = getDate()
    print(currentTransaction.date)
    currentTransaction.notes = getNotes()
    print(currentTransaction.notes)


main()
