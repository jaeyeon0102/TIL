-- Active: 1752639458321@@localhost@3306@sns_system_db
CREATE DATABASE sns_system_db
    DEFAULT CHARACTER SET = 'utf8mb4';
USE sns_system_db;

CREATE TABLE users (
  user_id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
)

CREATE TABLE posts (
  post_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255),
  content TEXT,
  creatd_at DATETIME,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
)


CREATE TABLE comments (
  comment_id INT PRIMARY KEY AUTO_INCREMENT,
  content TEXT,
  created_at DATETIME,
  user_id INT NOT NULL,
  post_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (post_id) REFERENCES posts(post_id)
)

