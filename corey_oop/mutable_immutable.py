'''
An immutable object is an object whose state cannot be modified after it is created. This is in 
cintrast to a mutable object, which can be modified after it is created.
'''

'''STRING IS IMMUTABLE'''
# a = 'corey'
# print(a)
# print('Address of a is: {}'.format(id(a)))


# # a[0] = 'C' # type error, string object does not support item assignment
# # print(a)
# a = 'John'
# print(a)
# print('Address of a is: {}'.format(id(a)))

################################################################

'''INTEGRE IS MUTABLE'''
a = [1, 2, 3, 4, 5]
print(a)
print('Address of a is: {}'.format(id(a)))


a[0] = 6 # type error, string object does not support item assignment
# print(a)
# a = 'John'
print(a)
print('Address of a is: {}'.format(id(a)))




