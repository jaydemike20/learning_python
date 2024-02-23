employee_1 = {"Name": "Frank", "Position": "Sales Representative", "Email Address": "frank@company.com"}

for key, value in employee_1.items():
    print(key)
    print(value)


# getting all keys
    
for key in employee_1.keys():
    print(key)

# values()

for value in employee_1.values():
    print(value)


cat = {
    1: {
        "name": "Sweetie",
        "age": 12,
        "color": "white",
    },
    2: {
        "name": "Ethnel",
        "age": 3,
        "color": "orange",
    },
}

print(cat[2]['name'])


for x, j in cat.items():

    print(x)
    
    for a, b in j.items():
        print(a, b)
    