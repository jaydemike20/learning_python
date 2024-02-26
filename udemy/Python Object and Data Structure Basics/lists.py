# list [] 

my_list = [1, 2, 3]
my_list = ['STRING', 100, 32.50, True]

print("Total lenght of my_list is {0}".format(len(my_list)))

my_list2 = ['one', 'two', 'three']

# indexing
print(my_list2[1:])

# combine list 
another_list = ['four', 'five']

combined_list = my_list2 + another_list
print(combined_list)

# mutate an index
combined_list[0] = 'ONE ALL CAPS'

print(combined_list)

# append list or add another index(value) on last index
combined_list.append('six')

print(combined_list)

combined_list.append('seven')

print(combined_list)

# pop() deleting the last index
combined_list.pop()
print(combined_list)

# remove index on specific path
combined_list.pop(0)
print(combined_list)

# sort and reverse
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

# arranged alphabetically

# it returns nonetype
my_sorted_list = new_list.sort()
print(my_sorted_list)

# to store it 
new_list.sort()
my_sorted_list = new_list

print(my_sorted_list)


# reverse
num_list.reverse()
print(num_list)

# coding exercise
print('\n\nCoding Exercise \n\n')

code_list = (1, 'two', 3,14159)

print(code_list)