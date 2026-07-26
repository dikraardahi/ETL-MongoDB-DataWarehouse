import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv("retail_sales_dataset.csv")

# Affichage des 5 premières lignes
print("===== Aperçu des données =====")
print(df.head())

# Colonnes
print("\n===== Colonnes =====")
print(df.columns)

# Dimensions
print("\n===== Dimensions =====")
print(df.shape)

# Types des colonnes
print("\n===== Types =====")
print(df.dtypes)

# Valeurs manquantes
print("\n===== Valeurs manquantes =====")
print(df.isnull().sum())

# Recherche des doublons
print("\n===== Doublons =====")
print(df.duplicated().sum())

# Conversion de la colonne Date

df["Date"] = pd.to_datetime(df["Date"])

print("\n===== Type après conversion =====")
print(df["Date"].dtype)

print("\n===== Informations générales =====")
print(df.info())

print("\n===== Statistiques =====")
print(df.describe())