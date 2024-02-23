
class User:

    # register account
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

        print(f"Your account is registed, Thank you for using this service {self.username} ")

    # login
    def login(self, username, password):
        
        if username is self.username and password is self.password:
            print("You're Login")
        else:
            print("Your Username or Password is Incorrect")


    