def askUser():
    username = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    checkPass(username, password)

def checkPass(user, pwd):
    if user == "username" and pwd == "password":
        login(user)
    else:
        print "Your username and/or password was incorrect"
        askUser()

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
        askUser()
    else:
        print "Unknown command"
        askCom()

askUser()
