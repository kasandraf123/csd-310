
\sql
\connect root@localhost
use whatabook


DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY '@Kf122397141159';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

CREATE DATABASE whatabook;
SHOW DATABASES;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(45)     NOT NULL,
    details     VARCHAR(500),
    author      VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('0', '510 E Word ST Refugio TX 78377');

INSERT INTO store(locale)
    VALUES('1', '896 S Roca ST Allen TX 78565');

/*
    insert book records 
*/
INSERT INTO book(book_id, book_name, details, author)
    VALUES('758', 'Life Force', 'Medicinal Advances', 'Tony Robbins');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('789', 'The Secret History', 'Modern Classic', 'Donna Tartt');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('790', 'Crime and Punishment', 'Guilt', 'Fyodor Dostoevsky');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('791', 'Jane Eyre', 'Gothic', 'Charlotte Bronte');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('792', 'Brave New World', 'Tech', 'Aldous Huxley');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('793', 'Wide Sargasso', 'Classic', 'Charlotte Bronte');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('794', 'One Hundred Years of Solitude', 'Realism', 'Gabriel Marquez');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('795', 'The Great Gatsby', 'American Dream', 'F. Scott Fitzgerald');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('796', 'Pride and Prejudice', 'Philosophy', 'Jane Austen');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('797', 'The Rainbow Fish', 'Youth', 'Marcus Pfister');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Kass', 'Figueroa');

INSERT INTO user(first_name, last_name)
    VALUES('Marlene', 'Delgado');

INSERT INTO user(first_name, last_name)
    VALUES('Alexander', 'Valdez');

/* SELECT * FROM whatabook.wishlist; */

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        0, 796
    );
    
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        0, 795
    );

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        0, 793
    );

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        0, 791
    );
