print('...rock...')
print('...paper...')
print('...scissors...')
p1 = input('Enter Player 1\'s choice:')
p2 = input('Enter Player 2\'s choice:')
print('Shoot!')
if p1 == p2:
    print('Its a tie!')
elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
    print('player1 is the winner!')
else:
    print('player2 is the winner!')


