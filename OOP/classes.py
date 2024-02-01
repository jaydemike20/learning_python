# OOP - Object Oriented Programming
# it aims to implement real world objects / entities its atributes and behavior into Programming 
# https://www.youtube.com/watch?v=Ej_02ICOIgs

# complex concepts
# attributes - objects, method kinds, encapsulation, polymorphism, abstraction, abstract classes


# store management system

class Item:

    def __init__(self):
        print("I am created")

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 5

