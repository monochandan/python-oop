############################################################################################
# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity

# # each data type is an object , that has instansiated earlier by some class

# print(type(item1)) # instansiated from string type of class  : <class 'str'>
# print(type(item1_price)) #  instansiated from int type of class  : <class 'int'>
# print(type(item1_quantity)) #  instansiated from int type of class  : <class 'int'>
# print(type(item1_price_total)) #  instansiated from int type of class  : <class 'int'>
# # print(type(item1))

# output:

# <class 'str'>
# <class 'int'>
# <class 'int'>
# <class 'int'>

# ## create datatype of our own
##############################################################################################

# 1. create class
# 2. create instance of class
# 3. magic function __init__
# 3. Instance attributes
# 3. create function in class
# 4. dynamic attributes
# 5. validate data types
# 6. assert : match what is happening with the expectations
# 7. Class attributes
# 8. magic function __repr__ : representing the object (ALSO TASKE LOOK ON __str__)
# 9. instantiate from csv
# 10. using decorator @classmethod
# 11. using decorator @staticmethod
# 12. difference of static and class methos  -> helper.py
# 13. inheritance
# 14.  super function - get acces all funtionalities of parent class into the child class
# 15. using the parent class attributes (all = [])
# 16. createing multiple py file for different class
# 17. ENCAPSULATION -  read only attributes (one opportunity to set the name, not changable)
# 18. _name : the variable has no seter
# 19. __name : private variable (could not acces outside the scope e.g - outside the class)
# 20. private method
# import csv

# class Item: # create a class
#     pay_rate = 0.8 # class atribute, after discount
#     all = [] # storing all instances in the list
#     def __init__(self, name:str, price:float, quantity = 0): # magic method
#         # Run validation to the received arguments
        
#         assert price >= 0, f"Price {price} is not greater than zero"
#         assert quantity >= 0, f"Price {quantity} is not greater than zero"

#         # print(f"An instances created: {name}")
#         # DYNAMIC ATTRIBUTES
#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         # actions to execute
#         Item.all.append(self)

        

#     def calculate_total_price(self): # METHOD = functions inside a class
#         # self : python passes the object itself (item1) as first argument, when we call the methods
#         return self.price * self.quantity 
    
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate # for all item same discount
#         # IF I USE ITEM.PAY_RATE; IT TAKES CLASS ATTRIBUTE BY DEFAULT
#         # BUT IF I CHANGE IT TO SELF:PAY_RATE; IT TAKES THE INSTANCE LEVEL VALUE (0.7)
#         # for diff item , diff discount

#     # METHOD TO TAKE CLASS REFERERENCE AS FIRST ARGUMENT (cls)
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('items.csv', 'r') as f:
#             reader = csv.DictReader(f) # read the csv as alist of dictionary
#             items = list(reader) # convert into a list
#             #print(items)

#         for item in items:
#             for k, v in item.items():
#                 #print(f"k:{k}")
#                 #print(f"v: {v}")
#                 keys = k.split(' ')
#                 keys = keys[0].split('\t')
#                 values = v.split(' ')
#                 values = values[0].split('\t')
#                 # print(f"keys: {keys}")
#                 # print(f"values: {values}")
#                 # print('#'*20)
#                 Item(
#                     name = values[0],
#                     price = float(values[1]),
#                     quantity = int(values[2])
#                 )
#             # Item(
#             #     name = 
#             # )
#     @staticmethod
#     def is_integer(num):
#         # we will count out that floats that are point zero 5.0 ,10.0
#         if isinstance(num, float):
#             # count out the floats that are point zero 5, 10
#             return num.is_integer()
#         elif isinstance(num, int):
#             return True
#         else:
#             return False

#     def __repr__(self): # return a string to represent the object
#         # return f"Item('{self.name}', {self.price}, {self.quantity})"
#         # after inheriting this class, lets try something else
#         return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


# item1 = Item("Phone", 100, 5) # create some instances of our class, just like as random variable : a = 10

# each one of this attributes (name, price) are assign to one instance (item1) of the class Item

# AFTER DYNAMIC ATTRIBUTE DELCARATION; WE CAN DELETE THIS ATTRIBUTES; JUST WE HAVE 
# TO PASS THE VALUE INSIDE THE INSTANCE; AMOUNT SHOULD BE SAME AS DYNAMIC VARIABLES 

# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5


# Item.instantiate_from_csv()# access the class method
# print(Item.all)

# print(Item.is_integer(7.0)) # access the stratic method
# print(Item.is_integer(7.5)) # access the stratic method




# print(item1.calculate_total_price(item1.price, item1.quantity))

# item2 = Item("Laptop", 1000, 3) # create some instances of our class, just like as random variable : a = 10

# AFTER DYNAMIC ATTRIBUTE DECLARATION WE CAN DELETE THIS ATTRIBUTES
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

# print(item2.calculate_total_price(item2.price, item2.quantity))

# print(type(item1)) # have created our own data type
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))
# item2.has_numpad = False
## output

# <class '__main__.Item'>
# <class 'str'>
# <class 'int'>
# <class 'int'>

# DYNAMIC ATTRIBUTES
# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(Item.pay_rate) # class attributes
# print(item1.pay_rate) # FIRST SEARCHED IN INSTANCE LEVEL; BUT DIDNOT FIND; THAN WENT FOR CLASS LEVELE AND GET THE VALUE
# print(item2.pay_rate) # FIRST SEARCHED IN INSTANCE LEVEL; BUT DIDNOT FIND; THAN WENT FOR CLASS LEVELE AND GET THE VALUE

# print(f"CLASS LABEL ATTRIBUTES: {Item.__dict__}\n")
# print(f"INSTANCE LABEL ATTRIBUTES: {item1.__dict__}\n")

# item1.apply_discount()
# print(f"price of {item1.name} afetr {item1.pay_rate * 100} % discount : {item1.price}")


# # DIFFERENT DISCOUNT FOR ITEM" PRODUCT
# item2.pay_rate = 0.7  # overriding the class attribute for this instance particularly, in instance level
# print(f"before discount {item2.price}")
# item2.apply_discount()
# print(f"After discount {item2.pay_rate * 100}%: {item2.price}")

# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all) # after declaring __repr__ [we can modify the list of representation of instances how we want]

# for instance in Item.all:
#     print(instance.name)



##################################INHERITENCE####################################################
# class Phone(Item): # inherit frome Item
#     # all = [] # leter using to append  -> Phone.all.append(self)
#     def __init__(self, name:str, price:float, quantity = 0, broken_phones = 0): # magic method
#         # call to super function to have access to all attributes / methods
#         super().__init__(
#             # special arguments coming from item class
#             name, price, quantity
#         )
#         # Run validation to the received arguments
#         assert broken_phones >= 0, f"Price {broken_phones} is not greater than zero"

#         # print(f"An instances created: {name}")
#         # DYNAMIC ATTRIBUTES
#         # Assign to self object
#         # self.name = name
#         # self.price = price
#         # self.quantity = quantity
#         self.broken_phones = broken_phones

#         # # actions to execute
#         # Phone.all.append(self)


# phone1 = Phone("jscPhonev10", 500, 5, 1)
# # phone1.broken_phones = 1
# # print(phone1.calculate_total_price())
# # phone2 = Phone("jscPhonev20", 700, 5, 1)
# # print(phone2.calculate_total_price())
# # phone2.broken_phones = 1

# print(Phone.all)
# print(Item.all)


#######################################MULTIPLE FILES#############################################

from item import Item
from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)

item1 = Item("MyItem", 750, 6)

# setting an attribute
# item1.price = 100
# print(item1.price)

# # getting an attribute
# # print(item1.name)

# item1.apply_increament(0.2)
# item1.apply_discount()
# print(item1.price)


# item1.send_email()
