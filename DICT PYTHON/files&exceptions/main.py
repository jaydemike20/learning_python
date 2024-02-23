# files are the named locations where you securely store your data
# two types of files : binary and text

# binary files are used for storing media files, compile code, or app data.
# text files are readable to us. (ex. plain text, source code)

# open(filename, mode)
# 4 modes (r, a, w, x)
# read = r
# append = a
# write = w
# create = x

# if na create na, dili na pwede tawagon balik
# f = open("newfile.txt", 'x')

# writing a file
f = open('newfile.txt', 'w')
f.write('Python is easy!')

# read mode
f = open("newfile.txt", 'r')
print(f.read())

f.close()

# append a file 
f = open('newfile.txt', 'a')
f.write("\nPython Intermediate")

# read mode
f = open("newfile.txt", 'r')
print(f.read())

f.close()