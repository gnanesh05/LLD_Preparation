from Library import Library
from Book import EBook
from Author import Author

library = Library("new library")

book1 = EBook("book1", Author("gnanesh"))
book1.get_details()
library.add_book(book1)