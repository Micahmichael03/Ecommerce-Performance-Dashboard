CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE online_retail (
    InvoiceNo VARCHAR(10),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice DECIMAL(10,2),
    CustomerID INT,
    Country VARCHAR(50),
    TotalPrice DECIMAL(10,2)
);

select * from online_retail