# when to use static method and when to use class method

class Item:
    pass

    @staticmethod
    def is_integer(self):
        '''
        - This should be do something that has a relationship with the class, 
        but not something that must be unique per instamce!

        - This method have nothing to do with instance.
        '''
    @classmethod
    def instantiate_from_something(clas):
        '''
        This should also do something that has a relationship with the class, 
        but usually, those are used to manipulate different structures of 
        data to instantiate objects, like we have done with csv.
        '''

    '''
    MAIN DIFFERENCE:
        static methods are not passing the object reference (e.g - self, cls) as the first argumet in the background.
    '''
    '''
    class method and static method could only be called from the class level. 
    But however, those also could be called from instances. (32-34)
    But there is no reason to call this methods from instance level
    '''


item1 = Item() # NO REASON
item1.is_integer() # NO REASON
item1.instantiate_from_something() # NO REASON



'''
ENCAPSULATION: 
    restricting the direct access to some of our attributes in a programm.

POLYMORPHISM (many forms):
    refres to use single type entity to represent different types in different scenario

INHERITANCE:
    child class inherit parent class behaivour

ABSTRACTION: 
    showe necessary attributes and hide the unnecessary attributes.
'''

