import os

# file = open('newfile.txt', 'w')
# file.write("Python is Easy")

# file = open('newfile.txt', 'a')
# file.write('\nBe a pythonnaire.')
# file.write('\nBy Creating an application in real life')
# file.write('\nTo become a billionaire')

# file = open('newfile.txt', 'r')
# print(file.read())

# file.close()

# 2
# file = open('newfile.txt', 'r')
# print(file.read())
# print(file.readline())

# for x in file:
#     print(x)

# file.close()

# if os.path.exists('newfile.txt'):
#     os.remove("newfile.txt")
# else:
#     print("The file doesn't exist")

# 3

# x = 500

# if x > 100:
#     raise Exception("This code will result in an error if x is bigger than 100")


# try:
#     print(variable_1)
# except:
#     print("Variable doesn't define")

# for i in range(6):
#     print("I'm so happy!")

# try:
#     print(12*6)
# except:
#     print("error")
# else:
#     print("Can performed")

best_burger = "Burger King"
number_2_burger = "McDonals"

assert best_burger == "McDonalds"
assert number_2_burger == "Burger King"