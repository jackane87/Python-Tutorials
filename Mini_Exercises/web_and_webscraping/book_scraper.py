import pyodbc
import requests
from bs4 import BeautifulSoup

#function scrapes all quotes
def scrape_books():
    all_books = []
    base_url = 'http://books.toscrape.com/'
    page = 'page-1.html'
    #Looping through pages while the next button is present to provide the url
    while page:
        #request quotes page based on concatenating base url and the href that gets updated from the next button.
        response = requests.get(f'{base_url}/catalogue/{page}').text
        #parsing the html returned
        soup = BeautifulSoup(response, 'html.parser')
        #finding all instances of the quote class on the page
        books = soup.select('.product_pod')
        #for each quote on the current page, appending the quote text, author, and author link as a dictionary to the quotes list.
        for book in books:
            book_data = (get_title(book), get_price(book), get_rating(book), get_instock(book))     #Can't get this to work at the moment.
            all_books.append(book_data)
        #finding the next button on the page
        next_btn = soup.find(class_='next')
        #set url to the href value for the next button if present; otherwise set value to None which is Falsy and will exit the while loop.
        page = next_btn.find('a').get('href') if next_btn else None
        #It is good practice when scraping to put in a wait between requests. Not needed for this exercise.
        #sleep(2)
    save_books(all_books)

def save_books(all_books):
    conn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}', server = 'JMOORE-P16S\SQLEXPRESS', database = 'PythonTesting')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO books (title, price, rating, instock) VALUES (?,?,?,?)", all_books)
    conn.commit()
    conn.close()

def get_title(book):
    return book.find('h3').find('a')['title']

def get_price(book):
    price = book.select('.price_color')[0].get_text()
    return float(price.replace("£","").replace("Â",""))

def get_rating(book):
    ratings = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    paragraph = book.select('.star-rating')[0]
    return ratings[paragraph.get_attribute_list('class')[-1]]

def get_instock(book):
    in_stock = (book.select('.instock.availability')[0].get_text()).strip()
    if in_stock == 'In stock':
        return 1
    return 0


scrape_books()

#created the table
#cursor.execute('''CREATE TABLE books(title varchar(40), price float, instock varchar(40), rating integer)''')