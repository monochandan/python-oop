'''
CLouser: A function that remembers the value in enclosing scope even if the scope is not present

A clouser is a record storing a function togather with an environment: 
a mapping associating each free variable of the function with the value or storage location to which the name was
bound when the clouser was created. A clouser, unlike a plain function, allows the function to access those captured
variables through the clouser's reference to them , even when the function is invoked outside their scope.

'''
# def outer_func(msg):
#     message = msg

#     def inner_function():
#         print(message) # message variabe is a free variable, we did not define it in inner function.
#     return inner_function

# my_func = outer_func('hi')
# your_func = outer_func('hello')
# # print(my_func.__name__)
# my_func()
# your_func()

################################################################################

import logging
logging.basicConfig(filename= 'example.log', level = logging.INFO)

def logger(func):
    def log_func(*args, **kwargs): # *args means any number of positional arguments, **kwargs means any number of keyword arguments
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
sub_logger(3, 3)