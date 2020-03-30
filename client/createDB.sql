CREATE DATABASE stockMarket;

USE stockMarket;

CREATE TABLE stock (
    ticker VARCHAR(7) NOT NULL,
    exchange VARCHAR(8) NOT NULL,
    PRIMARY KEY(ticker)
);

CREATE TABLE price (
    ticker VARCHAR(7) NOT NULL,
    date DATE NOT NULL,
    close FLOAT(5,2) NOT NULL,
    PRIMARY KEY(ticker,date)
);

CREATE TABLE buyNsell (
    buy_or_sell VARBINARY(4) NOT NULL,
    ticker VARCHAR(7) NOT NULL,
    date DATE NOT NULL,
    timestamp TIME NOT NULL,
    value FLOAT(6,2) NOT NULL,
    num_of_shares int(11) NOT NULL,
    PRIMARY KEY(ticker,date, timestamp)
);

INSERT INTO stock (ticker, exchange) VALUES
('AAPL','NASDAQ'),
('GOOG','NASDAQ'),
('IBM', 'NYSE'),
('JNJ','NYSE'),
('MSFT', 'NASDAQ'),
('TLRY', 'NYSE');

INSERT INTO price (ticker, date, close) VALUES
('AAPL', '2019-03-20', 100.00),
('AAPL', '2019-03-21', 101.50),
('AAPL', '2019-03-22', 106.50),
('GOOG', '2019-03-20', 100.00),
('GOOG', '2019-03-21', 130.00),
('GOOG', '2019-03-22', 110.00),
('IBM', '2019-03-20', 72.00),
('IBM', '2019-03-21', 70.00),
('IBM', '2019-03-22', 10.00),
('JNJ', '2019-03-20', 137.50),
('JNJ', '2019-03-21', 138.00),
('JNJ', '2019-03-22', 137.00),
('MSFT', '2019-03-20', 184.50),
('MSFT', '2019-03-21', 188.50),
('MSFT', '2019-03-22', 210.00),
('TLRY', '2019-03-20', 101.00),
('TLRY', '2019-03-21', 198.00),
('TLRY', '2019-03-22', 200.00);

INSERT INTO buyNsell (buy_or_sell, ticker, date, timestamp, value, num_of_shares) VALUES
('BUY', 'AAPL', '2019-03-20', '10:01:00', 99, 1000 ),
('BUY', 'AAPL', '2019-03-20', '11:22:00', 99.5, 1000),
('BUY', 'AAPL', '2019-03-21', '14:22:00', 100, 1000),
('SELL', 'AAPL', '2019-03-22', '12:18:00', 100, 2000),
('SELL', 'AAPL', '2019-03-22', '14:42:00', 103, 3000 ),
('BUY', 'GOOG', '2019-03-20', '12:22:00', 86, 2200 ),
('SELL', 'GOOG', '2019-03-20', '14:00:00', 87, 1000 ),
('SELL', 'GOOG', '2019-03-21','10:22:00', 87.5, 1000 ),
('BUY', 'GOOG', '2019-03-21', '13:28:00', 87, 800),
('SELL', 'GOOG', '2019-03-22', '11:45:00', 86, 500 ),
('BUY', 'IBM', '2019-03-20', '11:55:00', 273, 1100),
('BUY', 'IBM', '2019-03-21', '10:45:00' , 271, 2400),
('SELL', 'IBM', '2019-03-22', '12:09:00', 270.5, 250 ),
('BUY', 'MSFT', '2019-03-20', '11:45:00', 186, 1500),
('SELL', 'MSFT', '2019-03-21', '10:45:00', 188, 1000),
('BUY', 'MSFT', '2019-03-22', '12:03:00', 187, 5000);
