
# classmethod

# class InstanceCounter(object):
#     count = 0 # class variable

#     def __init__(self, val):
#         self.val = val
#         InstanceCounter.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val
    
#     @classmethod
#     def get_count(cls):
#         return cls.count
    
# a = InstanceCounter(5)
# b = InstanceCounter(13)
# c = InstanceCounter(17)

# for obj in (a, b, c):
#     print("val of obj: %s" % (obj.get_val()))
#     print("count: %s" % (obj.get_count()))


#14625

# static method
class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value
        
a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

print(a.val)
print(b.val)
print(c.val)