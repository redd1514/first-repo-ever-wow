import mysql.connector
from Challenge_1 import Book
from Challenge_2 import Ebook

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="challenge4"
        )
        self.cursor = self.conn.cursor()

    def save_book(self, book):
        sql = "INSERT INTO books (title, author, isbn, file_format) VALUES (%s, %s, %s, %s)"
        file_format = getattr(book, 'file_format', None)
        self.cursor.execute(sql, (book.title, book.author, book.isbn, file_format))
        self.conn.commit()

    def load_books(self):
        self.cursor.execute("SELECT title, author, isbn, file_format FROM books")
        books = []
        for title, author, isbn, file_format in self.cursor.fetchall():
            if file_format is None:
                books.append(Book(title, author, isbn))
            else:
                books.append(Ebook(title, author, isbn, file_format))
        return books
    

db = DatabaseManager(host='localhost', user='root', password='12345678', database='challenge4')

print("\nChallenge 4 Output: Database Interaction\n")

book = Book("Attack on titan", "Hajime Isayama", "99999")
ebook = Ebook("Tokyo ghoul", "Sui Ishida", "888888", "PDF")
newbook = Book("Chainsaw man", "Tatsuki Fujimoto", "123123")

db.save_book(newbook)
db.save_book(book)
db.save_book(ebook)


loadbooks = db.load_books()

for newbook in loadbooks:
    print(newbook)