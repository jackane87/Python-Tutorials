import requests
from bs4 import BeautifulSoup
from random import choice

#function scrapes all quotes
def scrape_quotes():
    all_quotes = []
    base_url = 'http://quotes.toscrape.com'
    url = '/page/1'
    #Looping through pages while the next button is present to provide the url
    while url:
        #request quotes page based on concatenating base url and the href that gets updated from the next button.
        request = requests.get(f'{base_url}{url}').text
        #parsing the html returned
        soup = BeautifulSoup(request, 'html.parser')
        #finding all instances of the quote class on the page
        page = soup.select('.quote')
        #for each quote on the current page, appending the quote text, author, and author link as a dictionary to the quotes list.
        for quote in page:
            all_quotes.append({"quote": f"{quote.find(class_='text').text}" , "author": f"{quote.find(class_='author').text}", "link": f"http://quotes.toscrape.com/{quote.find('a').get('href')}"})
        #finding the next button on the page
        next_btn = soup.find('li', attrs={'class': 'next'})
        #set url to the href value for the next button if present; otherwise set value to None which is Falsy and will exit the while loop.
        url = next_btn.find('a').get('href') if next_btn else None
        #It is good practice when scraping to put in a wait between requests. Not needed for this exercise.
        #sleep(2)
    return all_quotes


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





quotes = scrape_quotes()
play_game(quotes)

#get_hint('http://quotes.toscrape.com/author/John-Lennon/', 3)

#print(quotes)