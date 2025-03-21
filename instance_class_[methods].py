'''
instance methods - access aor modify the object state.
                    - instance variables inside a methods.
                    - Must have 'self' parameter to refer to the current object.
class methods - access or modify the class state.
                - In method only class variables.
                - Have 'class' parameter which refers to the class
'''

# EXAMPLE: instance method
class Student:
    def __init__(self, roll_no, name, age): # constructor to initialize instance variables
        # creatig instance attributes
        self.roll_no = roll_no
        self.name = name
        self.age = age

    def show(self): # instance method
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}")

    # creating instance attributes [before created in __init__()] in instance methode
    def add_marks(self, mark):
        self.mark = mark
    
    def update(self, roll_no, age):
        self.roll_no = roll_no
        self.age = age
        # print('Update successfull !!')

print("Class: VII")
emma = Student(15,"Jessa", 14) # creating a object to acces the class
emma.show() # call instance method

print("Class: VIII")
emma.update(5, 15)
emma.show()

emma.add_marks(75)
print(f"Roll No: {emma.roll_no}, Name: {emma.name}, Age: {emma.age}, Marks: {emma.mark}")


