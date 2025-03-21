class Base:
    def fun(self): # public method
        print('Public method of base class')

    def __fun(self): # private method
        print('Private method of base class')

    def access_private_method(self):
        print("Accessing private method \n")
        self.__fun()
    
class Derived(Base): 
    def __init__(self): # constructor of derived class
        # calling constructor of Base Class
        Base.__init__(self)
    
    def call_public(self):
        print('\n Inside derived class public method')
        self.fun()

    def call_private(self):
        print('\nInside derived class private method')
        self.__fun()

class A:
    def fun(self):
        print("Public method")
    def __fun(self):
        print("Private method")
    def help(self):
        self.fun()
        self.__fun()

# obj1 = Base()
# obj1.fun()
# obj1.access_private_method()

# obj2 = Derived()
# obj2.call_public()

# accessing the private method of a class using a public method of that class
# ob_a = A()
# ob_a.help()

# accessing the private method of a class using name mangling
# ob_a._A__fun()

# name mangling is helpful for letting subclass override methods without breaking interclass method calls
# for examples:
class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        self.__update(iterable)
    def update(self, iterable): # public method
        for item in iterable:
            self.item_list.append(item)

    __update = update # private copy of original update method

class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provide new signature for update
        # but doesnot break __init__()
        for item in zip(keys, values):
            self.item_list.append(item)

class MappingAnotehrSubclass(Mapping):
    def update(self, values):
        '''
            - GOAL IS TO ADD DUPLICATE FREE VALUES IN ITEM_LIST -
        - first previously stored list should be duplicate free.
        - new_list also be duplicate free
        - marge those two list , make self.item_list empty
        - than in self.item_list add the new duplicate free list with all duplicate free previous value 
            and current value.
        '''
        self.item_list = list(set(self.item_list)) # taking the previously added data when initialized the obj for this class
        print(f"self.item_list: {self.item_list}")
        # modifying the previous 
        lst = list(set(values)) # remove duplicate vakues from the list
        print(f"lst_: {lst}")
        final_list = list(set(lst + self.item_list))
        print(f"final list: {final_list}")

        self.item_list = []
        # print(lst)
        for item in final_list:
            self.item_list.append(item)

m = MappingSubclass([1, 2, 3]) # child class
# m1 = Mapping([7, 8, 9])# parent class

# print(m1.item_list)
# m1.update([10, 11])
# print(m1.item_list)

# print(m.item_list)
# m.update(['a', 'b'],[4, 5])
# print(m.item_list)

# m2 = MappingAnotehrSubclass([1, 2, 3, 4, 1, 4, 6])
# print(m2.item_list)
# m2.update([9, 10, 11, 10])
# print(m2.item_list)


############################### data type simmiler to the pascal 'record' or c 'struct'

from dataclasses import dataclass

@dataclass
class Employee:
    name:str
    dept:str
    salary:int 

john = Employee('John', 'computer lab', 1000)
print(john.dept)
print(john.salary)
    

