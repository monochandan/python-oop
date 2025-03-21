import types

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    def percentage(self, sub1, sub2):
        print(f"{self.name} got {(sub1 + sub2) / 2} %") 


'''
DYNAMICALLY ADD INSTANCE METHOOD - METHOD IS OUTSIDE THE CLASS
'''
def welcome(self):
    print("Hello", self.name, "Welcome to class IX")

s1 = Student("Jess", 17)

# adding instance method to object at runtime
s1.welcome = types.MethodType(welcome, s1)

s1.show()
s1.welcome() # calling the newly added instance method

s2 = Student("M", 25)
# s2 = s1.percentage(75, 65)

print(s1.percentage(65, 67))

''' DELET INSTANCE METHOD - del operator'''
# del s1.percentage

s2.show()
s2.welcome = types.MethodType(welcome, s2)
s2.welcome()

print(s2.percentage(50,30))

# print(s1.percentage(65, 67))

''' DELET INSTANCE METHOD - delattr() method'''
delattr(s1, 'percentage')
s1.show()
