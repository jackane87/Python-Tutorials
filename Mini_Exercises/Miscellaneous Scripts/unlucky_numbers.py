#this is the original way I coded this
'''for num in range(21):
    if num == 4 or num ==13:
        print(f'{num} is unlucky')
    elif num%2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')'''

#this is the cleaner way
for num in range(21):
    if num == 4 or num == 13:
        state = 'unlucky'
    elif num%2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{num} is {state}')
