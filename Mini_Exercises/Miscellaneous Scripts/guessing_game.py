from random import randint
comp_number = randint(1,10)
play_again = True
while play_again:
    guess = int(input('Guess a number between 1 and 10 '))
    #this loops while the user's guess does not match the computer's number
    while guess != comp_number:
        if guess < comp_number:
            print('Too low, try again! ')
            guess = int(input('Guess a number between 1 and 10 '))
        elif guess > comp_number:
            print('Too high, try again ')
            guess = int(input('Guess a number between 1 and 10 '))
    print('You guessed it! You won!')
    replay = input('Do you want to play again? Y/N ').upper()
    #If the user wants to replay, set play again to true, reset the computer number
    if replay == 'Y':
        play_again = True
        comp_number = randint(1,10)
    else:
        play_again = False
        print('Thanks for playing')
        break

