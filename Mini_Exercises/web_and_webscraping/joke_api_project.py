#The following three modules allow us to display the colorized ascii art.
from pyfiglet import figlet_format
from colorama import init
import termcolor
#Importing this module to use the random.choice method to pick a random joke from the list of returned jokes
import random
#This allows us to do the api request
import requests

print(termcolor.colored(figlet_format('Dad Jokes - O - Matic', font='isometric1'), color='green'))
url = "https://icanhazdadjoke.com/search"

tellanotherjoke = True

while tellanotherjoke:
    search_term = input('Let me Tell you a joke! Give me a topic: ').strip()
    response = requests.get(
        url, 
        headers={'Accept': 'application/json'},
        params={'term': search_term})

    data = response.json()
    if data['total_jokes'] == 0:
        print('There are not any jokes for that search criteria')
    else:
        random_joke = random.choice(data['results'])['joke']
        print(f'I\'ve got {data["total_jokes"]} about {search_term}. Here\'s one: ')
        print(random_joke)

    ask_for_another = input('Do you want to hear another joke? Y/N ').upper().strip()
    if ask_for_another != 'Y':
        print('Thanks for playing!')
        break
    else:
        pass
    
