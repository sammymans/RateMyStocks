CREATE DATABASE stonks;

USE stonks;

-- Test Table
DROP TABLE stocks_test;
CREATE TABLE stocks_test (
	ID int NOT NULL AUTO_INCREMENT,
    TickerSymbol VARCHAR(4) NOT NULL,
    CompanyName VARCHAR(255),
    price decimal(15,2),
    PRIMARY KEY (ID)
);

SELECT * FROM stocks_test;

INSERT INTO stocks_test (TickerSymbol, CompanyName, price)
VALUES ('AAPL', 'Apple Inc.', 245.33) 