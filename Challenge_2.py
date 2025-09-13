from Challenge_1 import Book

class Ebook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - Format: {self.file_format}"
    
print("\nThis is Challenge 2: Ebook Subclass \n")
book1 = Ebook("one punch man", "Gege Akutami", "99999", "PDF")
book2 = Ebook("Death note", "Tsugumi Ohba", "888888", "EPUB")

for book in (book1, book2):
    print(book) 