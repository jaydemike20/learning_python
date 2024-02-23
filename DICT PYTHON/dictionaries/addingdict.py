# ways of adding dictionaries

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


cat[3] = {}
cat[3]['name'] = "Tuna"
cat[3]['age'] = "5"
cat[3]['color'] = 'black'
cat[3]['ppersonality'] = "friendly"

cat[4] = {'name': 'Bubbles', 'age': '7', 'color': 'gray', 'personality': 'grumpy'}


for x, j in cat.items():
    print(j)