# encapsulation 46:03

# class MyClass(object):
#     def set_val(self, val):
#         self.value = val

#     def get_val(self):
#         return self.value
    

# a = MyClass()
# b = MyClass()

# a.set_val(100)
# b.set_val(200)

# # we can set attribute outside of class
# a.value = 'hello'

# print(a.get_val())
# print(b.get_val())

# another set of example


# encapsulation - refers to the safe storage of data (as attributes) in an instance.


# class MyInteger(object):
#     def set_val(self, val):
#         try:
#             val = int(val)
#         except ValueError:
#             return
        
#         self.val = val

#     def get_val(self):
#         return self.val
    
#     def increment_val(self):
#         self.val = self.val + 1


# i = MyInteger()
# i.set_val(9)
# print(i.get_val())
# i.val = 'hi'
# print(i.get_val())
# print(i.increment_val())


# __init__ constructor

# class MyNum(object):

#     def __init__(self, value):
#         try:
#             value = int(value)
#         except ValueError:
#             value = 0

#         self.val = value

#     def increment(self):
#         self.val += 1  # self.val = self.val + 1

# dd = MyNum('hello')
# bb = MyNum(100)
# dd.increment()
# dd.increment()
# bb.increment()
# print(dd.val)
# print(bb.val)


# class attributes vs instance attributes

# class YourClass(object):
#     classy = 10     # class attribute

#     def set_val(self):
#         self.insty = 100           # instance attribue

# dd = YourClass()
# dd.set_val()

# print(dd.classy)
# print(dd.insty)

# 10240
# class InstanceCounter(object):
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         InstanceCounter.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val
    
#     def get_count(self):
#         return InstanceCounter.count

# a = InstanceCounter(5)
# b = InstanceCounter(13)
# c = InstanceCounter(17)

# for obj in (a, b, c):
#     print("val of obj: %s" % (obj.get_val()))
#     print("count: %s" % (obj.get_count()))


