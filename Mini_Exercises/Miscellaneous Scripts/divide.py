def divide(a,b):
    try:
        result = a / b
    except ZeroDivisionError as err:
        print('Do not divide by zero.')
        print(err)
    except TypeError as err:
        print('a and b must be ints or floats')
        print(err)
    else:
        print(f'a divided by b is {result}')

(divide(4,2))

divide(1,0)

divide('one',2)
