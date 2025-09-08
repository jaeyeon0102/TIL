-- Active: 1752639458321@@localhost@3306@normalization_db
CREATE DATABASE normalization_db
    DEFAULT CHARACTER SET = 'utf8mb4';

USE normalization_db;

CREATE TABLE users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(15) NOT NULL,
  email VARCHAR(50)
);


CREATE TABLE posts (
  post_id INT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  content TEXT, 
  user_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE comments (
  comment_id INT PRIMARY KEY,
  content TEXT, 
  user_id INT NOT NULL,
  post_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (post_id) REFERENCES posts(post_id)
)