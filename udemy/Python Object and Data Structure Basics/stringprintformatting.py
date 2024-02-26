# string interpolation

myName = 'Jayde Mike T. Engracia'

print('Hi '+ myName)

# two methods (.format() and f-strings)

first_name = 'Jayde Mike'
last_name = 'Engracia'

# .format() method
print('My firstname is {0} and lastname is {1}'.format(first_name, last_name))

# f-string method
print(f'My name is {first_name} while my lastname is {last_name}\n')

# float formatting follows "{value:width.precesion f}"

result = 100/777

print('The result was {r:10.3f}'.format(r =result))

name = 'Jose'

print(f"Hello, his name is {name}")

name = "Sam"
age = 3

print(f'{name} is {age} years old.')

print('{x} {y}'.format(x = 'Python', y='Rules'))