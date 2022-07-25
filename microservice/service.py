import rpyc

class PasswordService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs on connection

    def on_disconnect(self, conn):
        # guess

    def