from random import randint # random
import datetime # date

print(int(randint(1, 1000)))

# strftime
t = datetime.datetime(2021, 5, 17)
print(t.strftime("%B"))
print(t.year)