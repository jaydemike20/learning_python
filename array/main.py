# array 

fruits = ["banana", "orange", "watermelon"]
exclude_orange = []

for x in fruits:

    if x is not "orange":
        exclude_orange.append(x)

else:
    print("Here are the list fruits that store in fruits variable")
    print(exclude_orange)
    print(fruits)


