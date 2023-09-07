from typing import List  # tuple, set, dict, etc

def list_avg(sequence: List) -> float:
    return sum(sequence)/ len(sequence)


#example of type hinting at work
list_avg(123)





class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count - page_count

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f'BookShelf with {len(self.books)}'