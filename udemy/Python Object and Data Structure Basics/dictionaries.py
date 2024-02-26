# dictionaties are unordered mappings for storing objects

# dictionaries objects retrieved by key name. (Unordered and can not sorted)
# lists objects retrieved by location. (Ordered Sequence can be indexed or sliced)

my_dict = {'key1': 'value1', 'key2': 'value2'}

# get all key-value pairs
print(my_dict)
# get value by providing keys
print(my_dict['key1'])

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}

print(prices_lookup['apple'])

d = {'k1': 123, 'k2':[0,1,2], 'k3':{'insideKey': 100}}

print(d['k3']['insideKey'])

e = {'key1': ['a', 'b', 'c']}
print(e)

print(e['key1'][2])
my_letter = e['key1']
letter = my_letter[2]

letter = letter.upper()
print(letter)


d = {'k1': 100, 'k2': 200}

# adding another keyvalue pair
d['k3'] = 300
print(d.keys())
print(d.items())
print(d.values())

# coding exercise
coding_dict = {'Apple': 25, 'Banana': 5, 'Carrots': 10}
print(coding_dict)