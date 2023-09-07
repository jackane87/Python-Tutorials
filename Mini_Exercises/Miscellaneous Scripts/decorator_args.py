def shout(fn):
    #by setting parameters to *args and **kwargs, we can accept any number of arguments or keyword arguments respectively.
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f'Hi, I\'m {name}.'

@shout
def order(main, side):
    return f'Hi, I\'d like {main} and {side} please.'

#these are examples of passing in arguments. by having *args set in the wrapper function, the order function, which has 2 parameters, will work.
print(greet('james'))
print(order('Steak', 'Potatoes'))

#this is an example of **kwargs being used. This would not work without **kwargs being a parameter of the wrapper function.
print(order(side='Steak', main='Potatoes'))