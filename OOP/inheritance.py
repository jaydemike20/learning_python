
# class Date(object):       # inherits from the 'objects' class 
#     def get_date(self):
#         return '2014-10-13'

# class Time(Date):           # inherits from 'date' class
#     def get_time(self):
#         return '08:13:07'
    
# dt = Date()
# print(dt.get_date())

# tm = Time()
# print(tm.get_time())
# print(tm.get_date())            # found this method in the Date class


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s!' % (self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print('%s goes after the %s' % (self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print('%s shreds the string %s' % (self.name))

r = Dog('Rover')
f = Cat('Fluffy')

r.fetch('paper')        
f.swatstring()
r.eat('dog food')
f.eat('cat food')

