HOW TO INITIALIZE RPYC:
    This uses RPyC, which is quite simple to set up on the client side.
    At the top of your program, add a line that says "import rpyc" (no quotation marks)
    In the body of your program, before you use the service, add the following:
        c = rpyc.connect("localhost", 22122)
    Note that you don't actually have to call it c, you can name the variable anything you want.
    The rest of this README will assume you named it c.
    Once this is done, and you're ready to use the service, run service.py.

HOW TO REQUEST DATA:
    In order to request password validation, use the following call:
        correct = c.root.validatePassword(userInput)
    "correct" and "userInput" also can be named whatever you like.
    "correct" represents a boolean value, explained later.
    "userInput" represents what the user entered for a password, as obtained by your program.

    In order to change the password, you can make almost the same call:
        correct = c.root.validatePassword(userInput, newPass)
    "correct" and "userInput" are the same as before.
    "newPass" represents what the user entered to change the current password to.
    Note that an attempt to change the password will fail if userInput is not the correct password.

HOW TO RECEIVE DATA:
    The validatePassword function will return True or False, dependent on whether userInput matched the stored password.
    This is true regardless of whether the password was changed or just checked.

WARNING:
    The password is stored in plaintext, on a file called "innocuous.txt" in the same directory as service.py.
    This is, obviously, not up to proper security standards. Amanda, if you like, I can work on actual encryption,
    but for an application like this, "mildly unsafe" is probably fine. If service.py's host machine is compromised,
    there's probably going to be larger concerns.
    The default password is "Cryptography", and the service will create innocuous.txt if it does not exist.
    For obvious reasons, probably change the password the first time you run the service.