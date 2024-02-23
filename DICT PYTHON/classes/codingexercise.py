
# 1
# class Customers:

#     greeting = "Welcome to Cofee Palace!"   # class variable

#     def __init__(self, name, beverage, food, total):
#         self.name = name
#         self.beverage = beverage
#         self.food = food
#         self.total = total




# g_1 = Customers('Nate', 'Expresso', 'Pastrami on rye', 220)
# g_2 = Customers('Elaine', 'Strawberry frappucino', 'Tuna wrap', 270)
# g_3 = Customers('Samirah', 'Iced Caffe Latte', 'Cinnamon Roll', 225)
# g_4 = Customers('Jerry', 'Caramel Macchiato', 'Glazed Dougnut', 230)
# g_5 = Customers('Paz', 'Iced Tea', 'Blueberry Pancakes', 315)


# print(Customers.greeting)



# inheritance


# 2
class ClubMembers:

    def __init__(self, name, birthday, age, favoritefood, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favoritefood = favoritefood
        self.goal = goal

    def printAll(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite Food", self.favoritefood)
        print("Goal", self.goal)

class ClubOfficers(ClubMembers):

    def __init__(self, name, birthday, age, favoritefood, goal, position):
        self.position = position
        super().__init__(name, birthday, age, favoritefood, goal)

    def printAll1(self):
        super().printAll()
        print("Position:", self.position)

m_1 = ClubMembers("Tom", "January 16", 14, "Ice Cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef Stroganoff", "To be the world's greatest chef", "Treasurer")

m_1.printAll()
o_4.printAll1()