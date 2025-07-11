# E-commerce Performance Dashboard

## Description
This project features a Power BI dashboard designed to analyze e-commerce sales data from the [Online Retail dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail) provided by the UCI Machine Learning Repository. The dashboard tracks key performance indicators (KPIs) such as total revenue ($6.49M), average order value ($475.72), and number of orders (14K). I customized it with additional visuals, including a customer district table and an order quantity donut chart, to provide deeper insights into customer behavior and sales patterns.

## Dataset
The dataset contains transactional data from a UK-based online retailer, covering December 2010 to December 2011. It includes details like invoice numbers, product codes, quantities, prices, customer IDs, and countries.

## Requirements
- Python 3.x
- MySQL
- Power BI Desktop
- Python libraries: `pandas`, `mysql-connector-python`, `ucimlrepo`

## Setup
1. **Database Setup:**
   - Install MySQL and create a database named `ecommerce_db`.
   - Run the SQL script `create_table.sql` to create the `online_retail` table:
     ```sql
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
     ```

2. **Data Loading:**
   - Run the ETL script to extract, transform, and load the data into MySQL:
     ```bash
     python etl_script.py
     ```

3. **Power BI:**
   - Open the `ecommerce_dashboard.pbix` file in Power BI Desktop.
   - Connect the data source to your MySQL database (`localhost`, `ecommerce_db`).

## Dashboard Features
- **Key Metrics:** Count of records (278.51K), number of orders (14K), average order value ($475.72), total revenue ($6.49M), total unit price ($879.56K), and quantity by distinct (266).
- **Revenue Trend Over Time:** Line chart showing quarterly revenue from Q4 2010 to Q4 2011.
- **Top Products by Revenue:** Horizontal bar chart highlighting top products like “Emergency CA” and various bike models.
- **CustomerID by District:** Custom table listing customers, their districts, and revenue (e.g., District 1 customers with $80-90 revenue).
- **Number of Orders by Year:** Pie chart comparing order volumes between 2010 and 2011.
- **Sales by Region:** Geographical map showing sales distribution across North America, Europe, Asia, and more.
- **Total Orders of Quantity:** Donut chart illustrating the distribution of order quantities.

## Visuals
![Dashboard Screenshot](screenshots.png)

## Insights
- Revenue peaked in Q2 2011, possibly due to seasonal demand or promotional campaigns.
- Products like “Emergency CA” and bikes are major revenue drivers, suggesting a focus on outdoor or sports equipment.
- The customer district table identifies high-value customers and regions for targeted marketing.
- The sales map reveals a diverse international customer base, useful for global expansion strategies.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests for enhancements or bug fixes.

## License
This project is licensed under the MIT License.