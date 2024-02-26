# String is immutable

name = "Sam"

# name[0] = 'P' #leads error


# concatenation
last_letters = name[1:]

print('P' + last_letters)

x = "Hello World "

print(x + "it is beautiful outside!")


letter = 'z'

print(letter*10)

# print(2 + '2') #typeError since datatypes are not the same


# method (uppercase, lowercase, capitalize , ... etc)
x = x.upper()

print(x)

# split method meaning it separate the words in a sentence
print(x.split())

y = 'Hi this is a string'

# removing i in the sentence use split(i)
print(y.split('i'))

