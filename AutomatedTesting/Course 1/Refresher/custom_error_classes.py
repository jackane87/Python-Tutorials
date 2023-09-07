
#This is a custom error class that inherits from the ValueError class.
class TooManyPagesReadError(ValueError):
    #we can just put pass here because where it is raised we enter a specific message.
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f'<Book {self.name}, read {self.pages_read} out of {self.page_count} pages.'
        )
    
    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f'You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages.'
            )
        self.pages_read += pages
        print(f'You have now read {self.pages_read} out of {self.page_count} pages.')


python101 = Book('Python 101', 50)
try:
    python101.read(20)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)
