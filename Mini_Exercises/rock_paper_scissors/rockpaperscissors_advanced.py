from random import randint

print('...rock...')
print('...paper...')
print('...scissors...')
p1 = input('Enter your choice:').lower()
comp = None
x = randint(0,2)
if x == 0:
    comp = 'rock'
elif x == 1:
    comp = 'paper'
else:
    comp = 'scissors'

print(f'The computer played: {comp}')


if p1 == comp:
    print('Its a tie!')
elif (p1 == 'rock' and comp == 'scissors') or (p1 == 'scissors' and comp == 'paper') or (p1 == 'paper' and comp == 'rock'):
    print('player1 is the winner!')
elif (comp == 'rock' and p1 == 'scissors') or (comp == 'scissors' and p1 == 'paper') or (comp == 'paper' and p1 == 'rock'):
    print('You lost to the computer!')   
else:
    print('Oooops something went wrong!')


