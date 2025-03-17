from item import Item


class Phone(Item): # inherit frome Item
    # all = [] # leter using to append  -> Phone.all.append(self)
    def __init__(self, name:str, price:float, quantity = 0, broken_phones = 0): # magic method
        # call to super function to have access to all attributes / methods
        super().__init__(
            # special arguments coming from item class
            name, price, quantity
        )
        # Run validation to the received arguments
        assert broken_phones >= 0, f"Price {broken_phones} is not greater than zero"

        # print(f"An instances created: {name}")
        # DYNAMIC ATTRIBUTES
        # Assign to self object
        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.broken_phones = broken_phones

        # # actions to execute
        # Phone.all.append(self)
