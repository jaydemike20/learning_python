# # make two lists: one for flavors
# flavors = ['vanilla', 'chocolate', 'strawberry', 'cookies \'n cream', 'bubblegum']
# toppings = ['almonds', 'banana slices', 'chocolate syrup', 'caramel syrup', 'white chocolate chips']

# combined = dict(zip(flavors, toppings))

# print(combined)

# combined['chocolate'] = 'blueberries'

# print(combined)

# # new flavors
# new_flavors = ['matcha', 'ube']
# new_toppings = ['pistachios', 'mango slices']

# new_combination = dict(zip(new_flavors, new_toppings))
    
# # adding keyvalue pair on dictionaries use update()
# combined.update(new_combination)

# print(combined)

# 2
groceries = {"chicken": 8, "apples": 6, "cucumbers": 3, "milk": 2, "oranges": 4}

groceries.pop('oranges')
print(groceries)

speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}

print(speakers.keys())


result = {"Carl": 'passed', "Quentin": 'failed', "Jonh Y": 'passed', "Peter": 'failed', "Max T.": 'passed', "Joseph": 'passed', "Jone": 'failed', "Jorge": 'failed', "George": 'passed', "Ben": 'passed', "Jerome": 'passed',
          "Rick": 'failed', 'Max G.': 'failed', 'John P.': 'failed', "Vince": 'passed'}


find = result.get('Jorge')

print(find)
