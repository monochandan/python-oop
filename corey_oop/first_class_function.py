'''
first_class function:
A programming language said to have first class functions if it treats functions as first class citizens.

first class citizen (programming):
A first class citizen (sometimes called first class objects) in a programming language 
is an entity which supports all the operations generally available to other entities.
These operations typically include being passed as an argument, returned from a function, 
and assigned to a variable.
'''
# def square(x):
#     return x*x

# f = square
# print(square)
# print(f(4))
#####################################
# def square(x):
#     return x*x

# def cube(x):
#     return x*x*x

# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# squares = my_map(cube, [1, 2, 3, 4, 5])

# print(squares)

##################################################

# def logger(msg):

#     def log_message():
#         print('log: ', msg)
#     return log_message # no parenthesis, we are not calling the function, we are returning the function

# log_hi = logger('Hi')
# log_hi()

#########################################################
def html_tag(tag):
    
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text
'''
set the variable tag as h1, so each time when we call the html_function to wrap the text message, it will remember
that we have set  the tag veriable to h1. Until we change the tag variable. 
'''
print_h1 = html_tag('h1')
print_h1('Head Line')
print_h1('Anotehr Headline')

print_p = html_tag('p')
print_p('This is paragraph')
