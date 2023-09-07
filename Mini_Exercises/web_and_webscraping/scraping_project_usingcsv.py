import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

def read_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)




#function runs the game
def play_game(quotes):
    play_again = True
    clue_number = 1
    while play_again:
        game_quote = choice(quotes)
        print(game_quote['quote'])
        for i in reversed(range(1,5)):
            guess = input(f'Who Said this? Guesses ramaining: {i} ')
            if guess.lower() == game_quote['author'].lower():
                print('You guessed correctly! Congratulations!')
                break
            elif i > 1: 
                get_hint(game_quote['link'], clue_number)
                clue_number += 1
            else:
                print(f"Sorry, the correct answer is {game_quote['author']}")
        play_again = input('Would you like to play again (y/n)? ')
        if play_again.lower() in ('y', 'yes'):
            play_again = True
            clue_number = 1
        else:
            play_again = False
            print('Thanks for playing!')

#function returns the hints for the guessing game
def get_hint(url, clue_number):
    #getting the html for the author page and parsing it
    request = requests.get(url).text
    soup = BeautifulSoup(request, 'html.parser')
    name = soup.find(class_='author-title').text.split()
    if clue_number == 1:
        #Clue indicating when the author was born and whre is presented
        print(f"Author born on {soup.find(class_='author-born-date').text} {soup.find(class_='author-born-location').text}")
    elif clue_number == 2:
        #Clue indicating what the author's first name starts with.
        print(f"The author's first name starts with: {name[0][0]}")
    else:
        #Clue indicating what the author's last name starts with.
        print(f"The author's last name starts with: {name[len(name)-1][0]}")





quotes = read_quotes('quotes.csv')
play_game(quotes)

#get_hint('http://quotes.toscrape.com/author/John-Lennon/', 3)

#print(quotes)