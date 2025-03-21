'''
DIFFERENCE BETWEEN INSTANCE METHOD CLASS METHOD  STATIC METHOD
-- instance method:
    - bound to the object of a class
    - it can modify a object state
    - can acces and modify both class and instance variables, has 'self' as first veriable
-- class method:
    - Bound to the class
    - it can modify a class state
    - can access only class variables, has cls as first parameter
    - used to creaete factory methods
    -- @classmethod decorator or classmethod() function
-- static method:
    - bound to the class
    - it can not modify a class or object state
    - can not access or modify the class and instance variables, thats why no 'self' or no 'cls' as first parameter
    - @staticmethod decorator or staticmethod() function
'''

class Student:
    school_name = 'Trier School'

    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age
        self.school_name = Student.school_name

    def show(self):
        # print(self.name, self.age, Student.school_name) #p1
        print(f"Name: {self.name}, Age: {self.age}")
        # accessing the class variables
        if self.school_name != Student.school_name:
            print(f"{self.name} has changed the School to: {self.school_name}") #p2
        else:
            print(f"{self.name}'s School Name: {self.school_name}")

    
    @classmethod # school name change for all students
    def change_school(cls, name):
        print(f"Previous School name: {cls.school_name}") #p2
        cls.school_name = name
        print(f"School name changed to {cls.school_name}")

    # school name change for individual student
    def indi_change_school(self, name):
        # print()
        self.school_name = name

    @staticmethod
    def find_notes(subject_name):
        #p2 can not access instance or class level attributes
        return ['chapter 1', 'chapter 2', 'chapter 3']

#p1  Method call
# instance method   
# jessa = Student('jessa', 14)
# jessa.show()

# # class method
# Student.change_school('XYZ School')
# jessa.change_school('ABC School')

# # static method
# print(Student.find_notes('Math'))
# print(jessa.find_notes('Math'))


#p2 attribute access
jessa = Student('jessa', 12)
# call instance methods
jessa.show()

# call class method
jessa.indi_change_school('XYZ_School')
jessa.show()

tessa = Student('Tessa', 13.5)
tessa.show() # it will

print(jessa.show is tessa.show) # FALSE - seperate copy for seperate objects - TAKE MORE MEMORY
print(jessa.find_notes is tessa.find_notes) # TRUE - same copy for different object - TAKE LESS MEMORY








