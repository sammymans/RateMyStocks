CREATE DATABASE stockdatabase;
USE stockdatabase;

DROP TABLE IF EXISTS yahoo_prices_for_stocks;

-- CREATE TABLE stockinfo (
-- Date DATE, 
-- Symbol VARCHAR(4) NOT NULL,
-- High DECIMAL(15,2),
-- Low DECIMAL(15,2), 
-- Open DECIMAL(15,2), 
-- Close DECIMAL(15,2), 
-- Volume DECIMAL(15,1), 
-- AdjClose DECIMAL(15,2)
-- );


INSERT INTO yahoo_prices_for_stocks (Date, Symbol, High, Low, Open, Close, Volume)
VALUES ('2001-01-01', 'AAPL', 1.22, 1.22, 1.22, 1.22, 2);

SELECT * FROM yahoo_prices_for_stocks;

-- add row number to the table so we can see the number of entries
SELECT row_number() OVER() AS num_row,
Date, 
Symbol,
High,
Low, 
Open, 
Close, 
Volume
FROM yahoo_prices_for_stocks
