from pymongo import MongoClient

uri = "mongodb+srv://USERNAME:PASSWORD@cluster0.xxxxx.mongodb.net/"

client = MongoClient(uri)

print(client.list_database_names())

print("Connexion réussie")
