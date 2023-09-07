def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    return dividend/divisor

#divide(15, 0)


students = [
    {'name': 'bob', 'grades': [75, 90]},
    {'name': 'rolf', 'grades': [70]},
    {'name': 'jen', 'grades': [100, 90]}
]


try:
    for student in students:
        name = student['name']
        grades = student['grades']
        average = divide(sum(grades),len(grades))
        print(f'{name} averaged {average}')
except ZeroDivisionError as e:
    #print(e)
    print(f'ERROR: {name} has no grades')
else:
    print('--- All student averages calculated ---')
finally:
    print('--- All student averages calculated ---')
