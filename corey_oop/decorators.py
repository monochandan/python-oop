'''
WE CAN EASILY ADD FUNCTIONALITIES (fun) TO OUR EXISTING FUNCTIONS. 
That fun will be be defined in a wrapper function.

1. CLOUSERS
2. basic decorator
3. python decorator
4. function decoration
5. classd ecorator
6. practical examples
7. multiple decorators
8. multiple decorators with original function name 
'''
def outer_function(msg):
    # message = msg

    def inner_function():
        '''we can access teh mssg variable even though
        it is not in the inner function scope'''
        print(msg)
    return inner_function

'''my_func is equal to inner function waiting to be exicuted'''
# my_func = outer_function()
hi_finc = outer_function('Hi')
bye_func = outer_function('Bye')
hi_finc()
bye_func()
##########################################################################

def decorator_function(original_function):
    def wrapper_function():
        '''
         original function wrappes with wrapper function
        '''
        print('wrapped by me!')
        return original_function()
    return wrapper_function

''''display is decorated'''
@decorator_function
def display():
    print('display function ran')
'''
decorator_display == wrapper function. Which is waiting to be executed. 
'''
display() #  after putting @decorator_function

# other wise , if we dont use @decorator_function
decorated_display = decorator_function(display)
decorated_display()


##########################################
'''decorator function'''
def decorator_function(original_function):
    '''
    *args, **kwargs - accept any arbritary number of keywords and arguments
    '''
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before function: {}'.format(original_function.__name__))
        if args:
            print('args: ', args)
        if kwargs:
            print('kwargs: ', kwargs)
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))

display()
print('\n')
display_info('John', 25)

###########################################

'''class decorator'''
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before function: {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
    
@decorator_class
def display():
    print('display function ran')

@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))

obj = decorator_class()
display()
print('\n')
display_info('John', 25)

#########################################
''''practical examples'''

from functools import wraps
def my_logger(orig_func):
    import logging
    ''' 
    keep tracking, how many time a specific function run, what argument has 
    passed to that function.
    '''
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level = logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args:{}, and kwargs {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

def my_time(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper


@my_logger
def display():
    print('display function ran')

@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))

import time 
@my_logger
@my_time
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({},{})'.format(name, age))

display()
print('\n')
display_info = my_time(display_info)
print(display_info.__name__)
display_info('Hank', 45)
##########################################

def decorator_function(original_function):
    def check_variables(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return original_function(a, b)
        else:
            raise ValueError('Not integer')
    return check_variables
def take_integer_to_add(a, b):
    return a + b

decorated_add = decorator_function(take_integer_to_add)

print(decorated_add('a', 'b'))



