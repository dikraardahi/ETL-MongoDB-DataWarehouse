import pandas as pd
import sqlite3
import requests
from pymongo import MongoClient

from pymongo import MongoClient
from urllib.parse import quote_plus

from datetime import datetime



uri = "mongodb+srv://USERNAME:PASSWORD@cluster0.xxxxx.mongodb.net/"

client = MongoClient(uri)

db = client["etl_warehouse"]

print("Connexion réussie")

# =========================
# SOURCE 1 : CSV
# =========================

sales_df = pd.read_csv("retail_sales_dataset.csv")

sales_collection = db["sales_data"]

sales_collection.delete_many({})

sales_collection.insert_many(
    sales_df.to_dict("records")
)

print("CSV chargé")

# =========================
# SOURCE 2 : API
# =========================

url = "https://api.open-meteo.com/v1/forecast?latitude=34.02&longitude=-6.84&current=temperature_2m"

response = requests.get(url)

data = response.json()

weather_doc = {
    "time": data["current"]["time"],
    "temperature": data["current"]["temperature_2m"]
}

weather_collection = db["weather_data"]

weather_collection.delete_many({})

weather_collection.insert_one(weather_doc)

print("API chargée")

# =========================
# SOURCE 3 : SQLITE
# =========================

conn = sqlite3.connect("sales.db")

products_df = pd.read_sql_query(
    "SELECT * FROM products",
    conn
)

products_collection = db["products_data"]

products_collection.delete_many({})

products_collection.insert_many(
    products_df.to_dict("records")
)

conn.close()

print("SQLite chargée")


log_collection = db["pipeline_logs"]

total_records = (
    len(sales_df)
    + len(products_df)
    + 1
)

log_document = {
    "run_date": datetime.now(),
    "status": "SUCCESS",
    "records_processed": total_records
}

log_collection.insert_one(log_document)

print("ETL terminé avec succès")
