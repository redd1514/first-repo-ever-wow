from Challenge_1 import Book
from Challenge_2 import Ebook

class Library:
    def __init__(self):
        self.books = []
        self._index = 0 

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        self._index = 0  
        return self

    def __next__(self):
        if self._index < len(self.books):
            result = self.books[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

library = Library()
book1 = Book("Bleach", "Makoto Yukimura", "9781612620244")
book2 = Ebook("Ippo Makunochi", "Takehiko Inoue", "9781421521500", "EPUB")

library.add_book(book1)
library.add_book(book2)

print("\nChallenge 3 Output: Library Iteration\n")

for book in library:
    print(book)

