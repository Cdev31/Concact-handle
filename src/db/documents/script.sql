
CREATE DATABASE contactdb; 

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone_number VARCHAR(12) NOT NULL,
    CONSTRAINT CHECK_EMAIL CHECK ( email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
    CONSTRAINT CHECK_PHONE_NUMBER CHECK ( phone_number REGEXP '^[0-9]{4}-[0-9]{4}$' )
);

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(20) NOT NULL,
    phone_number VARCHAR(12) NOT NULL,
    user INT NOT NULL,
    CONSTRAINT CHECK_CONTACT_PHONE_NUMBER CHECK ( phone_number REGEXP '^[0-9]{4}-[0-9]{4}$' ),
    CONSTRAINT FK_USER FOREIGN KEY ( user ) REFERENCES users( id )
);