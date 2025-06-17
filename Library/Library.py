from typing import List
from Book import Book

class Library:
    def __init__(self, name):
        self.name = name
        self.books: List[Book] = [] 

    def add_book(self, book:Book):
        self.books.append(book)
    
    def print_books(self):
        for book in self.books:
            print(f"book title -{book.name} genre - {book.type} written by {book.author}")

