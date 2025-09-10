-- Active: 1752639458321@@localhost@3306@library_db
CREATE DATABASE library_db;

USE library_db

CREATE TABLE authors (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100)
)

INSERT INTO authors (name)
VALUES
('J.K. Rowling'),
('George R.R. Martin'),
('J.R.R. Tolkien'),
('Isaac Asimov'),
('Agatha Christie')

CREATE TABLE genres (
  id INT PRIMARY KEY AUTO_INCREMENT,
  genre_name VARCHAR(100)
)

INSERT INTO genres (genre_name)
VALUES
('Fantasy'),
('Science Fiction') ,
('Mystery'),
('Thriller')

CREATE TABLE books (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(100),
  author_id INT NOT NULL,
  genre_id INT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES authors(id),
  FOREIGN KEY (genre_id) REFERENCES genres(id)
)

CREATE INDEX idx_authors_name ON authors(name);

SHOW INDEX FROM authors;

CREATE INDEX idx_genres_name ON genres(genre_name);

INSERT INTO books (title, author_id, genre_id)
VALUES
('Harry Potter and the Philosopher\'s Stone',
  (SELECT id FROM authors WHERE name = 'J.K. Rowling'), 
  (SELECT id FROM genres WHERE genre_name = 'Fantasy')
), 
('A Game of Thrones',
  (SELECT id FROM authors WHERE name = 'George R.R. Martin'), 
  (SELECT id FROM genres WHERE genre_name = 'Fantasy')
), 
('The Hobbit',
  (SELECT id FROM authors WHERE name = 'George R.R. Martin'), 
  (SELECT id FROM genres WHERE genre_name = 'Fantasy')
), 
('The Lord of the Rings',
  (SELECT id FROM authors WHERE name = 'J.R.R. Tolkien'), 
  (SELECT id FROM genres WHERE genre_name = 'Fantasy')
), 
('Foundation',
  (SELECT id FROM authors WHERE name = 'Isaac Asimov'), 
  (SELECT id FROM genres WHERE genre_name = 'Science Fiction')
), 
('I, Robot',
  (SELECT id FROM authors WHERE name = 'Isaac Asimov'), 
  (SELECT id FROM genres WHERE genre_name = 'Science Fiction')
), 
('Murder on the Orient Express',
  (SELECT id FROM authors WHERE name = 'Agatha Christie'), 
  (SELECT id FROM genres WHERE genre_name = 'Mystery')
), 
('The Mysterious Affair at Styles',
  (SELECT id FROM authors WHERE name = 'Agatha Christie'), 
  (SELECT id FROM genres WHERE genre_name = 'Mystery')
), 
('The Girl with the Dragon Tattoo',
  (SELECT id FROM authors WHERE name = 'Agatha Christie'), 
  (SELECT id FROM genres WHERE genre_name = 'Thriller')
)