# getting a key

exam_scores = {"Jonathan": 85, "Erica": 99, "Rose": 83, "Henry": 92, "Missy": 77,
               "Ashleigh": 88, "Paul": 60, "Gordon": 86, "Lisa": 90, "Kelly": 77,
               "Joe": 65, "Tiffany": 67, "Wesley": 97, "Gail": 71}

print(exam_scores['Paul'])

check_key = "Andrew"

if check_key in exam_scores:
    print(check_key, "took the test")
else:
    print(check_key, "didn't took the test")


# .get() method shows us the key we're looking for. If it doesn't exists, return none
print(exam_scores.get("Lisa"))
print(exam_scores.get("Wesley"))
print(exam_scores.get("Quennie"))


# .pop()
neighbors = {"Mr. Santos": "Fruitcake", "Mr. Reyes": "Cookies",
             "Mrs. Dela Cruz": "cupcakes", "Mr.Tiu": "gingerbread man"}

done = neighbors.pop("Mr. Reyes")
y = neighbors.keys()
z = neighbors.values()
m = neighbors.items()

print(y)
print(z)
print(m)