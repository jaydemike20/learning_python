f = open("newfile.txt")

f = open("newfile.txt", "r")


# reading specific parts of a file
# print(f.read(202))

# reading by a single line
# print(f.readline())

for x in f:
    print(x)

f.close()