import csv
class Item: # create a class
    pay_rate = 0.8 # class atribute, after discount
    all = [] # storing all instances in the list
    def __init__(self, name:str, price:float, quantity = 0): # magic method
        # Run validation to the received arguments
        
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Price {quantity} is not greater than zero"

        # print(f"An instances created: {name}")
        # DYNAMIC ATTRIBUTES
        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)
    
    @property # restricting the access of attribute price
    def price(self):
        return self.__price
    
    def calculate_total_price(self): # METHOD = functions inside a class
        # self : python passes the object itself (item1) as first argument, when we call the methods
        return self.__price * self.quantity 
    
     
    def apply_discount(self): # METHOD = functions inside a class
        # self : python passes the object itself (item1) as first argument, when we call the methods
        self.__price = self.__price * self.pay_rate  

     
    def apply_increament(self, increament_vaue): # METHOD = functions inside a class
        # self : python passes the object itself (item1) as first argument, when we call the methods
        self.__price = self.__price  + self.__price * increament_vaue

    @property
    # property decorator = read only attribute
    def name(self):
        print('in property method')
        return self.__name

    @name.setter # still want to set new value for the variable name (before failed, declaring property method)   
    def name(self, value):
        print("trying to set a new value: setter")
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate # for all item same discount
        # IF I USE ITEM.PAY_RATE; IT TAKES CLASS ATTRIBUTE BY DEFAULT
        # BUT IF I CHANGE IT TO SELF:PAY_RATE; IT TAKES THE INSTANCE LEVEL VALUE (0.7)
        # for diff item , diff discount

    # METHOD TO TAKE CLASS REFERERENCE AS FIRST ARGUMENT (cls)
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) # read the csv as alist of dictionary
            items = list(reader) # convert into a list
            #print(items)

        for item in items:
            for k, v in item.items():
                #print(f"k:{k}")
                #print(f"v: {v}")
                keys = k.split(' ')
                keys = keys[0].split('\t')
                values = v.split(' ')
                values = values[0].split('\t')
                # print(f"keys: {keys}")
                # print(f"values: {values}")
                # print('#'*20)
                Item(
                    name = values[0],
                    price = float(values[1]),
                    quantity = int(values[2])
                )
            # Item(
            #     name = 
            # )
    @staticmethod
    def is_integer(num):
        # we will count out that floats that are point zero 5.0 ,10.0
        if isinstance(num, float):
            # count out the floats that are point zero 5, 10
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self): # return a string to represent the object

        # return f"Item('{self.name}', {self.price}, {self.quantity})"
        # after inheriting this class, lets try something else
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    # @property
    # def read_only_name(self):
    #     return "AAA"
    def __connect(self, smtp_server):
        pass

    
    def __prepare_body(self):
        return f""" Hello,
                we have {self.name} {self.quantity} times.
                Regards,        
        """
    def __send(self):
        pass

    def send_mail(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

