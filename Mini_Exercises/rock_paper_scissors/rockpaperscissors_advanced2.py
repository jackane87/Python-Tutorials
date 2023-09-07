from random import randint
player_wins = 0
computer_wins = 0
num_ties = 0
winning_score = 3
while True:
    while player_wins < winning_score and computer_wins <winning_score:
        print(f'Player Score: {player_wins}   Computer score: {computer_wins}')
        print('...rock...')
        print('...paper...')
        print('...scissors...')
        p1 = input('Enter your choice: ').lower()
        comp = None
        x = randint(0,2)
        if x == 0:
            comp = 'rock'
        elif x == 1:
            comp = 'paper'
        else:
            comp = 'scissors'

        print(f'The computer played: {comp}')
        if p1 == 'quit' or p1 == 'q':
            break
        elif p1 == comp:
            print('Its a tie!')
            num_ties += 1
        elif (p1 == 'rock' and comp == 'scissors') or (p1 == 'scissors' and comp == 'paper') or (p1 == 'paper' and comp == 'rock'):
            print('Player won that round!')
            player_wins += 1
        elif (comp == 'rock' and p1 == 'scissors') or (comp == 'scissors' and p1 == 'paper') or (comp == 'paper' and p1 == 'rock'):
            print('Computer won that round!')
            computer_wins += 1   
        else:
            print('Oooops something went wrong!')
    if player_wins > computer_wins:
        print('Congratulations you won the game!')
    elif player_wins == computer_wins:
        print('It\'s a Draw!')
    else: 
        print('Game Over! You Lost!')
    print(f'Final Scores...Player: {player_wins}   Computer: {computer_wins} Draws: {num_ties}')
    replay = input('Do you want to play again? Y/N ').upper()
    if replay == 'Y':
        computer_wins = 0
        player_wins = 0
        num_ties = 0
    else:
        print('Thanks for playing!')
        break


