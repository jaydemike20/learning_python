# an exception is an object which tells you about the problem you encountered. 
# It also provides a traceback which tells you where you made a blunder on your code.

# raise keyword, syntax error, assertions, zerodivisionerror, typeerror

# the raise keyword lets us define errors and the text that will be printed on the console when the specified error occurs.

# n = -5
# if n < 0:
#     raise Exception("No Negative Numbers Allowed")

# SyntaxError occurs when the code is not written correctly
# cats = 11
# if cats > 10
#     print("Are u fur-real")

# Assertions are boolean expressions that make sure that the conditions are true.
# employee_of_the_year = "Roger"

# assert employee_of_the_year == "Roger"

# assert employee_of_the_year == "Suzanne"

#ZeroDivisionError occurs when you divided by zero.
# 1/0

# TypeError occurs when an operation is performed on an incorrect or unsupported object type.
# a = 1
# b = "string"

# x = a + b

# 50 ** 'two'

# try and except - these blocks are used to spot and handle exceptions
# finally block allows us to run our code no matter what the resul of the try and except blocks.

# try:
#     print(x + "macarrons")
# except NameError:
#     print("Please Define your variable")
# except IndentationError:
#     print("Please be careful when indenting your code")
# except:
#     print("Something is wrong!")

# try:
#     print(500+4305)
# except:
#     print("This operation cannot be performed")
# else:
#     print("No issues here!")

try:
    print(h)
except:
    print("There's something wrong with our program")
finally:
    print("Let's run our program anyway.")
