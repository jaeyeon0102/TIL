CREATE DATABASE sns_system_db
    DEFAULT CHARACTER SET = 'utf8mb4';

USE sns_system_db;

CREATE TABLE users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255)
);

INSERT INTO users (name, email)
VALUES 
  ('홍길동', 'hong@example.com'),
  ('이순신', 'lee@example.com');


CREATE TABLE posts (
  post_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  title VARCHAR(255),
  content TEXT,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO posts (user_id, title, content)
VALUES 
  (1,'첫 번째 게시물 ', '안녕하세요'),
  (1,' 두 번째 게시물', '반갑습니다'),
  (2,' 세 번째 게시물', '좋은 하루');


CREATE TABLE comments (
  comment_id INT PRIMARY KEY,
  post_id INT NOT NULL,
  content TEXT,
  FOREIGN KEY (post_id) REFERENCES posts(post_id)
)

INSERT INTO comments (comment_id, post_id, content)
VALUES 
  (1001,4, '첫 댓글'),
  (1002,5, '두 번째 댓글'),
  (1003,6, '세 번째 댓글');


SELECT name, email FROM users;


SELECT p.title, p.content FROM posts p
JOIN users u ON p.user_id = u.user_id
WHERE u.name = '홍길동';


SELECT c.content FROM comments c
JOIN posts p ON c.post_id = p.post_id
WHERE p.title = '첫 번째 게시물 ';

INSERT INTO users (name, email)
VALUES ('김유신','kim@example.com')


UPDATE users
SET email = 'new_lee@example.com'
WHERE name = '이순신'