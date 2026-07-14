import numpy as np
import pandas as pd

link = 'https://raw.githubusercontent.com/QuantikDataStudio/dataset/main/property%20data.csv'

# 'na' (minuscule) et '--' ne sont pas reconnus par défaut : on les déclare comme
# marqueurs de valeurs manquantes, en plus de ceux déjà connus ('NA', 'n/a', 'NaN', '').
df = pd.read_csv(link, na_values=['na', '--'])

# affichage du dataframe avec valeurs manquantes
print(df)

# affichage des informations sur le dataframe
print(df.info())

# Cette fonction permet de déterminer les variables avec des valeurs manquantes
def valeur_manquante(df):
    flag=0
    for col in df.columns:
            if df[col].isna().sum() > 0:
                flag=1
                print(f'"{col}": {df[col].isna().sum()} valeur(s) manquante(s)')
    if flag==0:
        print("Le dataset ne contient plus de valeurs manquantes.")

valeur_manquante(df)

# Certaines colonnes numériques sont lues comme du texte à cause de valeurs parasites
# ('HURLEY'...). pd.to_numeric les convertit en nombres et transforme tout ce qui
# n'est pas convertible en NaN (errors='coerce').
NUMERIC_COLUMNS = ['PID', 'ST_NUM', 'NUM_BEDROOMS', 'NUM_BATH', 'SQ_FT']
for col in NUMERIC_COLUMNS:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# On garde une copie du dataframe AVEC ses valeurs manquantes, pour le 2e exemple.
# .copy() crée un dataframe indépendant : modifier `df` ne touchera pas `df_avec_na`.
df_avec_na = df.copy()

# --- Exemple 1 : REMPLACER les valeurs manquantes avec .replace() ---
# .replace(np.nan, valeur) remplace chaque NaN par `valeur`. Pour les colonnes
# numériques on utilise la moyenne de la colonne ; pour OWN_OCCUPIED (texte) la
# valeur la plus fréquente (le mode), une moyenne n'ayant pas de sens sur du texte.
for col in NUMERIC_COLUMNS:
    df[col] = df[col].replace(np.nan, df[col].mean())
df['OWN_OCCUPIED'] = df['OWN_OCCUPIED'].replace(np.nan, df['OWN_OCCUPIED'].mode()[0])
df['SQ_FT'] = df['SQ_FT'].replace(np.nan, df['SQ_FT'].mean())

print("\n--- Exemple 1 : valeurs manquantes remplacees par la moyenne (.replace) ---")
print(df)
valeur_manquante(df)

# --- Exemple 2 : SUPPRIMER les lignes contenant des valeurs manquantes avec .dropna() ---
# On repart de la copie qui contient encore les valeurs manquantes. .dropna()
# supprime toute ligne ayant au moins un NaN et renvoie un nouveau dataframe.
df_sans_na = df_avec_na.dropna()

print("\n--- Exemple 2 : lignes avec valeurs manquantes supprimees (.dropna) ---")
print(df_sans_na)
valeur_manquante(df_sans_na)
