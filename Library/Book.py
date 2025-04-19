from abc import ABC, abstractmethod
from Author import Author

class Book(ABC):
    def __init__(self,type, name, author: Author):
        self.type = type
        self.name = name
        self.author = author

    @abstractmethod
    def get_details(self):
        pass
       


class EBook(Book):
    def __init__(self, name,author):
        super().__init__("Ebook",name, author)

    def get_details(self):
         print(f"book name {self.name} by {self.author.name}")


class PrintedBook(Book):
    def __init__(self, name,author):
        super().__init__("PrintedBook", name, author)

    def get_details(self):
         print(f"book name ${self.name} by ${self.author.name}")
