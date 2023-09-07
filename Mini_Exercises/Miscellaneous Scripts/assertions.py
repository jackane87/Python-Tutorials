'''def add_positive_numbers(a, b):
    assert a > 0 and b > 0, 'Both numbers must be positive.'
    return a + b

print(add_positive_numbers(1,5))
add_positive_numbers(-2, 3)'''

def eat_junk(food):
    assert food in ['pizza', 'ice cream', 'candy', ' fried butter'], 'food must bee junk food.'
    return f'Nom nom, I\'m eating {food}'


food = input('Enter a food please: ')
print(eat_junk(food))