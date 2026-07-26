import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

query = "SELECT * FROM products"

products_df = pd.read_sql_query(query, conn)

print(products_df)

conn.close()