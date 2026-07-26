from pymongo import MongoClient

uri = "mongodb+srv://ADMIN:Admin123@cluster0.vvmibrv.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

print(client.list_database_names())

print("Connexion réussie")