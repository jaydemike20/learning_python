# class MyClass(object):
#     var = 10


# this_obj = MyClass()
# that_obj = MyClass()

# print(this_obj.var)
# print(that_obj.var)

# -------------------------------
# class Joe(object):
    
#     def callme(self):
#         print('calling "callme" method with instance')
#         print(self)

# thisjoe = Joe()

# thisjoe.callme()

# -------------------------------
# self is the instance of my class
# import random

# class MyClass(object):
#     def dothis(self):
#         self.rand_val = random.randint(1, 10)


# myinst = MyClass()
# myinst.dothis()
# print(myinst.rand_val)


# max size

# class MaxSizeList(object):

#     def __init__(self, max):
#         self.max = max
#         self.innerList = []

#     def push(self, obj):
#         self.innerList.append(obj)
#         if len(self.innerList) > self.max:
#             self.innerList.pop(0)

#     def get_list(self):
#         return self.innerList
    
# a = MaxSizeList(3)
# b = MaxSizeList(1)

# a.push('hey')
# a.push('hi')
# a.push('go')
# a.push("let's go")

# b.push('hey')
# b.push('hi')
# b.push('go')
# b.push("let's go")

# print(a.get_list())
# print(b.get_list())

# INHERITANCE

