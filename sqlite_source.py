import sqlite3

conn = sqlite3.connect("sales.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL
)
""")

cursor.execute("""
INSERT INTO products (product_name, category, price)
VALUES
('Laptop', 'Electronics', 1200),
('T-Shirt', 'Clothing', 25),
('Shampoo', 'Beauty', 10)
""")

conn.commit()

print("Base créée avec succès")

conn.close()