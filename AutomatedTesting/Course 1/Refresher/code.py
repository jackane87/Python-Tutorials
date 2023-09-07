class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book {self.name}, {self.book_type}, weighing {self.weight}g'
    
    @classmethod
    #This is a hardcover book constructor. Takes in the name and a page_weight
    def hardcover(cls, name, page_weight):
        #returns a book object with the passed in name, the hardcover value from the Types tuple and the page_weight + 100 to account for the hard cover.
        return Book(name, Book.TYPES[0], page_weight + 100)
    
    @classmethod
    #This is a paperback book constructor. Takes in the name and a page_weight
    def paperback(cls, name, page_weight):
        #returns a book object with the passed in name, the paperback value from the Types tuple and the page_weight.
        return Book(name, Book.TYPES[1], page_weight)


book = Book.hardcover('Harry Potter', 1500)
light = Book.paperback('Python 101', 600)


print(book.name)
print(book)
print(light)