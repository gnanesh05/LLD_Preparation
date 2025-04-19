from typing import List
from Book import Book

class Library:
    def __init__(self, name):
        self.name = name
        self.books: List[Book] = [] 

    def add_book(self, book:Book):
        self.books.append(book)

