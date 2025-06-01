import pandas as pd
import os

# Chemin du fichier original
fichier_original = "logements_sociaux_fr_propre.csv"

# Vérifier que le fichier existe
if not os.path.exists(fichier_original):
    print(f"⚠️ Fichier non trouvé : {fichier_original}")
    exit()

print("📥 Chargement du fichier...")
df = pd.read_csv(fichier_original)

# Diviser le DataFrame en deux moitiés
milieu = len(df) // 2
df1 = df.iloc[:milieu]
df2 = df.iloc[milieu:]

# Sauvegarder les deux fichiers
fichier1 = "logements_sociaux_fr_propre_part1.csv"
fichier2 = "logements_sociaux_fr_propre_part2.csv"

print(f"💾 Sauvegarde de la première moitié dans {fichier1}...")
df1.to_csv(fichier1, index=False)

print(f"💾 Sauvegarde de la seconde moitié dans {fichier2}...")
df2.to_csv(fichier2, index=False)

print("✅ Terminé : deux fichiers CSV créés.")