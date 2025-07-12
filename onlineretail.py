import pandas as pd
import mysql.connector
from mysql.connector import Error
# from ucimlrepo import fetch_ucirepo
# from sqlalchemy import create_engine

# Extract
print("Extracting data...")
csv_file_path = 'Online Retail.csv'
df = pd.read_csv(csv_file_path)

# Transform
print("Transforming data...")
df = df[~df['InvoiceNo'].str.startswith('C')]

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Calculate TotalPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice'] # adding new column

# Drop rows with missing CustomerID
df = df.dropna(subset=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country', 'TotalPrice']) # dropping missing value in this column

# Convert CustomerID to integer
df['CustomerID'] = df['CustomerID'].astype(int)

# Load
print("Loading data to MySQL...")
def batch_insert(df, table_name, batch_size=1000):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='ecommerce_db',
            user='root',
            password='your_password'
        )
        cursor = connection.cursor()
        columns = ', '.join(df.columns)
        placeholders = ', '.join(['%s'] * len(df.columns))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        data = [tuple(row) for row in df.itertuples(index=False, name=None)]
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            cursor.executemany(insert_query, batch)
            connection.commit()
            print(f"Inserted {i + len(batch)} rows into {table_name}")
        cursor.close()
        connection.close()
        print("Data loaded successfully.")
    except Error as e:
        print(f"MySQL Error: {e}")

batch_insert(df, 'online_retail')