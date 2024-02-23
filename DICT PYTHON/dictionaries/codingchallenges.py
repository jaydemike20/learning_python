# 1

students = ["Joy", "Asha", "Oscar"]
vocal_ranges = ["soprano", "alto", "tenor"]

singers = dict(zip(students, vocal_ranges))

print(singers)


# 2
teacher_info = {"Name": "Rina", "Subject": "Math"}

for key, value in teacher_info.items():
    print(key)
    print(value)


# 3
weather_in_asia = {"Japan":22, "Malaysia": 25, "Philippines": 48 }

# weather_in_asia.update({"Singapore": 27})
weather_in_asia["Singapore"] = 27

print(weather_in_asia)

# 3
