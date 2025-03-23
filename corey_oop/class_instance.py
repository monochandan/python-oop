# easy to re-use
class Employee: # class -  blue print of an instance
    # class variable
    raise_amount = 1.04
    num_of_employee = 0
    def __init__(self, first_name, last_name, pay): #constructor / initialize
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        # self.email = first_name + '.' + last_name + '@company.con'

        Employee.num_of_employee += 1 # instead of self using Employee, value will be same for all instance (its obvious !!)
    
    @property
    def full_name(self):
        return'{}.{}@email.com'.format(self.first_name, self.last_name)
    @property
    def email(self):
        '''@property - DEFINING AS A METHOD, BUT WANT TO ACCESS AS A ATTRIBUTE'''
        '''After chainging the name , the email dont chnage automatically sooo...ISSUE!!'''
        return'{} {}'.format(self.first_name, self.last_name)
    
    @full_name.setter
    def full_name(self, name):
        '''
        Can not set the attributes on @property method:
        AttributeError: property 'full_name' of 'Employee' object has no setter
        '''
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        '''delet'''
        print('Delete Name!')
        self.first_name = None
        self.last_name = None

    def apply_raise(self):
        '''
        self.raise_amount = give us the ability to raise amount for individual instance, raise_amount could be different
        Employee.raise_amount = the value will be same for all instance
        '''
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount): # common convention of class -> cls
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str): # alternative constructor
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # create new employee
    
    @staticmethod # dont operate on the instance or the class
    def is_workday(day):
        #  is the day is week day
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    def __repr__(self):
        '''MAGIC METHOD
        For more: https://docs.python.org/3/reference/datamodel.html#emulating-container-types
        '''
        return "Employee('{}','{}','{}')".format(self.first_name, self.last_name, self.pay)
    
    def __str__(self):
        '''MAGIC METHOD'''
        return '{} - {}'.format(self.full_name(), self.email)
    
    def __add__(self, other):
        '''MAGIC METHOD : Adding 2 employees salary togather'''
        return self.pay + other.pay
    def __len__(self):
        '''MAGIC METHOD'''
        return len(self.full_name())
    
class Developer(Employee):
    '''
    By chainging the raise_amount in the subclass. It didn't have any effect on any of our Employee instances.
    It will effect only the Developer instances. 

    '''
    raise_amount = 1.10
    
    def __init__(self, first_name, last_name, pay, prog_lang): #constructor / initialize
        # self.first_name = first_name
        # self.last_name = last_name
        # self.pay = pay
        # self.email = first_name + '.' + last_name + '@company.con'
        super().__init__(first_name, last_name, pay) ## useful for multiple inheritance
        # Employee.__init__(self, first_name, last_name, pay) # only one parent class inheritated
        self.prog_lang = prog_lang


class Manager(Employee):
    
        def __init__(self, first_name, last_name, pay, employees = None):
            super().__init__(first_name, last_name, pay)
            if employees is None:
                self.employees = []
            else:
                self.employees = employees

        def add_employee(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)

        def remove_employee(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)
        
        def print_emps(self):
            for emp in self.employees:
                print(' --->',emp.full_name())





 # print(Employee.num_of_employee) # 0

dev_1 = Developer('Corey', 'Schefer', 5000, 'Python')
dev_2 = Developer('c', 's', 23000, 'Java')


mgr_1 = Manager('sue', 'smith', 90000, [dev_1])

emp_1 = Employee('Corey', 'Schefer', 5000)
emp_2 = Employee('c', 's', 23000)


emp_1.first_name = 'Jim'
print(emp_1.first_name)
'''
emp_1's email has not changed, because it has initialized once, when the emp_1 was created. 
So now even we  changing the first name emp_1, it will not change the email varivale implicitly

'''
print(emp_1.email)
'''
@property - dont have to add email(). It will looks like attribute, 
but it is a function inside a class [thanks to @property decorator!!]
'''
print(emp_1.email)
print(emp_1.full_name)


'''
Can not set the attributes on @property method:
AttributeError: property 'full_name' of 'Employee' object has no setter

'''
emp_1.full_name = 'Mono Chandan'
print(emp_1.first_name)
# print(emp_1.last_name)
print(emp_1.full_name)
print(emp_1.email)

'''Delet the name using @property @full_name.deleter '''
del emp_1.full_name

print(emp_1.email)
print(emp_1.full_name)
print(emp_1.last_name)

print(emp_1)
print(repr(emp_1))
print(str(emp_1))

'''Dunder Method'''
print(emp_1.__repr__())
print(emp_1.__str__())
print(emp_1.__init__('first_name', 'last_name', 100))

print(emp_1.full_name())

'''Dunder Add'''
print(int.__add__(1, 2)) # same as print(1+2)

'''Dunder method to add 2 employees salary, function declared in the Employee class
original page: https://docs.python.org/3/reference/datamodel.html#emulating-container-types
'''
print(emp_1 + emp_2)

'''Dunder Method for getting the length of the emp name'''

print(len(emp_1.full_name()))

print(isinstance(mgr_1, Manager))# is the object is a instance of a class
print(isinstance(mgr_1, Employee))# is the object is a instance of a class
print(isinstance(mgr_1, Developer))# is the object is a instance of a class

print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))
print(mgr_1.email)
mgr_1.add_employee(dev_2)
mgr_1.remove_employee(dev_1)
mgr_1.print_emps()

# 
print(dev_1.email)
print(dev_1.prog_lang)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.email)
print(dev_2.email)
# 
print(help(Developer))
# 
# 
# 
import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
# 
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
# 
new_employee_1 = Employee.from_string(emp_str_1)
# 
new_employee = Employee(first, last, pay)
# 
print(new_employee_1.email)
print(new_employee_1.pay)
# 
Employee.set_raise_amt(1.05) #  equal to Employee.raise_amount = 1.04
# 
emp_1.set_raise_amt(1.05) #  change in class level, though we have called from instance level
# my explanation : 
#                 it could be because, emp_1 is instance of a Employee Blueprint
#                 # so python giving access to it to the Employee class to change it the class level variable by using
#                 # the class level  method


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# 
# 
# 
print(emp_1.num_of_employee) # 2
# 
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
# 
print(Employee.__dict__)
print(emp_1.__dict__)
# 
Employee.raise_amount = 1.05 # change all instance value
emp_1.raise_amount = 1.05 # only chnage the emp_1 value
# 
# 
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# 



















print(emp_1.email)
print(emp_2.email)
# 
print(emp_1.full_name())
print(Employee.full_name(emp_1))
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'abc'
emp_1.pay = 1000
# 
# 
emp_2.first = 'C'
emp_2.last = 'S'
emp_2.email = 'a'
emp_2.pay = 100
# 
print(emp_1.email)
# 
