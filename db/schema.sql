CREATE DATABASE db_posts
use db_posts;

DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO posts (title, content) VALUES ('First Post', 'Content for the first post');
INSERT INTO posts (title, content) VALUES ('Second Post', 'Content for the second post');
