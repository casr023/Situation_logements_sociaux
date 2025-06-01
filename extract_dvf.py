import pandas as pd

# Le chemin complet de mon fichier txt
chemin_fichier = "E:/Projet_SQL/valeursfoncieres-2024.txt"

# Lecture du fichier avec pandas, séparateur ; et encodage iso-8859-1 souvent utilisé pour ce genre de fichiers
df = pd.read_csv(chemin_fichier, sep=';', encoding='iso-8859-1', low_memory=False)

print(df.head())  # affiche les 5 premières lignes pour vérifier la lecture
print(f"Nombre de lignes : {len(df)}")
# Afficher les noms de colonnes
print("\nColonnes du fichier :")
print(df.columns)

# Afficher les types de données
print("\nTypes de données :")
print(df.dtypes)
