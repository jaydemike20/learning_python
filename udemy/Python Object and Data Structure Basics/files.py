# input/output and basic files

f = open('myfile.txt', 'w')

f.write('This is the first line\n')
f.write('This is the Second line\n')
f.write('This is the Third line\n')
f.write('This is the Fourth line\n')


f = open('myfile.txt', 'r')





myfile = open('/home/jaydee/Desktop/python/learning_python/myfile.txt', 'r')

# read txt without closing

with open('myfile.txt') as my_new_file:
    print(my_new_file.read())


with open('myfile.txt', mode ='a') as f:
    f.write("Four or Fourth")

with open('myfile.txt') as my_new_file:
    print(my_new_file.read())

with open('dhgksajdlakj.txt', mode='w') as f:
    f.write("\nI CREATED THIS FILE ")

with open('dhgksajdlakj.txt') as my_new_file:
    print(my_new_file.read())


# exercise
file = open('test.txt', mode='w')
file.write('Hello World')

file.close()