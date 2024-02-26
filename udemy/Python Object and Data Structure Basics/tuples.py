# tuples - immutability and it uses parenthesis
t = (1,2,3)
my_list = [1, 2, 3]

print(type(t))
print(type(my_list))

t = (1 ,2)
print(t[0])

t = ('a', 'a', 'b')

print(t.count('a'))
print(t.index('a'))
print(t.index('b'))

my_list[0] = 'NEW'
print(my_list)

