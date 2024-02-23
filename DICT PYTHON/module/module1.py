# def greeting(name):
#     print("Hey there, " + name + "! Ready to do some math?")

# using class

class User:

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

user_1 = User("Jayde", 22, "Philippines")
user_2 = User("Mike", 23, "Philippines")


def get_sum(x, y):
    return x + y

def get_dif(x, y):
    return x - y

def get_prod(x, y):
    return x * y

def get_quo(x, y):
    return x / y