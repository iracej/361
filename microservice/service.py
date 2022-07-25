import rpyc
import os.path
from rpyc.utils.server import ThreadedServer
from os.path import exists


class PasswordService(rpyc.Service):
    def __init__(self):
        if not os.path.exists("innocuous.txt"):
            f = open("innocuous.txt", "x")
            f.write("Cryptography")
    def on_connect(self, conn):
        print("Connection established.")

    def on_disconnect(self, conn):
        print("Connection terminated.")

    def exposed_validatePassword(self, userInput, change = None):
        f = open("innocuous.txt", "r")
        theTruth = f.read()
        f.close()
        if userInput == theTruth:
            if change is not None:
                self.changePassword(change)
            return True
        else:
            return False

    def changePassword(self, newPassword):
        f = open("innocuous.txt", "w")
        f.write(newPassword)
        f.close()


t = ThreadedServer(PasswordService, port=22122)
t.start()
