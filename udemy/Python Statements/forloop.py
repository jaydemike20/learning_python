# iterable means iterate

# syntax of a for loop

# example number 1
my_iterable = [1, 2, 3]

for item_name in my_iterable:
    print(item_name)

# example number 2
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(num)

# example number 3
for num in my_list:

    if num % 2 == 0:
        print(num)
    else:
        print('odd number: {0}'.format(num))

list_num = 0

for num in my_list:
    list_num = list_num + num

print('Sum of all element {0}'.format(list_num))

print('\n\n\n')


for letter in "Hello World":
    print(letter)


# tuple unpacking

tup = (1, 2, 3)

for item in tup:
    print(item)

mylist = [(1,2), (3,4) , (5,6), (7,8)]

print(len(mylist))

for a, b in mylist:
    print(a)
    print(b)


mylist = [(1,2,3), (4,5,6), (7,8,9)]

for a,b,c in mylist:
    print(b)

# iterate through dictionary
    
d = {'k1': 1, 'k2': 2, 'k3': 3}

for value in d.values():
    print(value)


# continue in 36. while loops
    