# dictionaries are like warehouse - key-value pairs

shopping_list = {
    "weird hat": 150, "purple rug": 450,
    "old books": 200, "stuffed elephant": 50
}


print(shopping_list["old books"])

# adding list
shopping_list["plastic ring"] = 20
shopping_list["stuffed elephant"] = 80

print(shopping_list)

# dictionaries list

basketball_teams = {"Crouching Tigers" : ["Jacob", "Kevin", "Roni", "Joshua", "Isagani"], "Hidden Dragons" : ["Ted", "Bryan", "Edu", "Luis", "Mark"]}

print(basketball_teams)

pets = {"Gerald": "Guinea Pig", "Alice": "dog", "Ruby": "cat"}

print(pets)

# update    
pets.update({"Ron": "gecko", "Paulina": "hamster", "Marlon": "goldfish"})
print(pets)

# combine two list into 1 dictionary
# zip function takes two or more lists and combines them
# dict function turns the combined list into a dictionary

relative = ["Tita Malou", "Jeff", "Tito Roger", "Veronica"]

age = [54, 14, 55, 19]

combined_lists = zip(relative, age)

relative_age = dict(combined_lists)

print(relative_age)