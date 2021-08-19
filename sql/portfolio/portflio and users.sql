DROP TABLE users;
CREATE TABLE users (
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);

DROP TABLE portfolio;
CREATE TABLE portfolio (
    ticker varchar(4),
    userid INT,
    purchase_date DATE, 
	shares int,
    purchase_price DECIMAL(15,2),
    
    FOREIGN KEY (userid) REFERENCES users(user_id)
);

insert into users (name) values ('Sammy Farnum');
insert into users (name) values ('Caleb Eom');

insert into portfolio (ticker, userid, purchase_date, shares, purchase_price)
values ('TSLA', 1, '2021-08-16', 10, 688.12);
insert into portfolio (ticker, userid, purchase_date, shares, purchase_price)
values ('AAPL', 2, '2021-08-16', 21, 241.55);
insert into portfolio (ticker, userid, purchase_date, shares, purchase_price)
values ('GOOG', 2, '2021-08-16', 33, 1242.27);
insert into portfolio (ticker, userid, purchase_date, shares, purchase_price)
values ('BA', 1, '2021-08-16', 42, 132.08);

SELECT * FROM users;
SELECT * FROM portfolio;