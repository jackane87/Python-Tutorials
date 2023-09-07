'''Write a function called only_ints which accepts a function and returns another function. 
The function passed to it should only be invoked if all of the arguments passed to it are integers. 
Otherwise the inner function should return "Please only invoke with integers.".'''

'''
@only_ints 
def add(x, y):
    return x + y
    
add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

from functools import wraps

#this was my solution
def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) for arg in args):
            return fn(*args, **kwargs)
        return 'Please only invoke with integers.'
    return wrapper


#this was the exercise solution 
#I think this solution is better than mine because if any of the args are NOT an int the function immediately returns the only integers message.
#In my solution, the entire args tuple has to be iterated over and each arg evaluated and if all are ints then return the function. This is less efficient.
def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return wrapper