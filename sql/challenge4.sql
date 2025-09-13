create database challenge4;
use challenge4;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    isbn VARCHAR(50),
    file_format VARCHAR(50) NULL
);

select * from books;