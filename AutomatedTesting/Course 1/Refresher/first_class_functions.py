#this is the first class function. it is passed into calculate as the 'operator' parameter
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0')
    return dividend/divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 5, operator=divide)

print(result)

##################################################################################################################

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f'Could not find an element with {expected}')


friends = [
    {'name': 'Rolf Smith', 'age': 24},
    {'name': 'Adam Wool', 'age': 30},
    {'name': 'Anne Pun', 'age': 27}
]

#this is the first class function for the second group of functions 
def get_friend_name(friend):
    return friend['name']


print(search(friends, 'Rolf Smith', get_friend_name))