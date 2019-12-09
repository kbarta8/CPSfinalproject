import re
import sys

def askUserFirst():
    print("Welcome to your IoT device! Please enter your login info: \n")
    username = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    checkDefPass(username, password)
    

def checkDefPass(user, pwd):
    if user == "admin" and pwd == "mydevice":
        firstLogin(user)
    else:
        print "Your username and/or password was incorrect"
        sys.exit()

def firstLogin(user):
    print "Welcome to your new device. For your security, please change your login information."
    user1 = ""
    rules = [user1 != "admin",
             user1 != "username",
             user1 != "user"]
    user1 = raw_input("Enter your new username: ")
    if (user1 != "admin"):
        pass1 = raw_input("Enter your new password: ")
        newUser(user1, pass1)
    else:
        print "Invalid username, please enter another.\n\n\n\n"
        firstLogin(user)

def newUser(username1, password1):
    print "For your additional security, please enter an email"
    print "This can be used to access your account if you forget your password"
    addr = raw_input("Enter your email: ")
    if isValidEmail(addr):
        print "Thank you for adding your email address. "
        login(username1)
    else:
        print "invalid email"
        newUser(username1, password1)

def isValidEmail(email):
 if len(email) > 7:
     if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
         return True
 return False
    
def login(user):
    print "Welcome " + user
    print "You are logged in."
    askCom()

def askCom():
    command = raw_input("Enter a command: ")
    if command == "log off" or command == "quit":
        username =  ""
        password = ""
        print "you are logged off"
        sys.exit()
    else:
        print "Unknown command"
        askCom()

askUserFirst()
