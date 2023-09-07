#This was my solution for the exercise. I did have to look at the solution for the looping logic to get all pages of quotes. 
#My original logic always omitted the last page of quotes because my while loop was looking for the presence of the next button. 
#My code would request the last page, but sine the next button wasn't present it would'nt run the for loop for the quotes.


import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

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
        next_btn = soup.find(class_='next')
        #set url to the href value for the next button if present; otherwise set value to None which is Falsy and will exit the while loop.
        url = next_btn.find('a').get('href') if next_btn else None
        #It is good practice when scraping to put in a wait between requests. Not needed for this exercise.
        #sleep(2)
    return all_quotes


quotes = scrape_quotes()

def write_quotes(quotes):
    with open('quotes.csv', 'w', encoding='utf-8') as file:
        headers = ['quote', 'author', 'link']
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

write_quotes(quotes)



