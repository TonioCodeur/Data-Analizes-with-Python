from pathlib import Path

import pandas as pd

data = Path(__file__).parent / 'drugs_consumption.csv'

df = pd.read_csv(data, sep=',', header=0)

# différentes méthodes pour récupérer les données
print(df.head())
print(df.tail())
print(df.describe(include='all'))
print(df.sample(10))
print(df.info())

# récupération d'une ligne
print(df.loc[5]) # récupération de la ligne 5

# récupération de plusieurs lignes
print(df.loc[5:10]) # récupération des lignes 5 à 10
print(df.loc[:]) # récupération de toutes les lignes

df_subutex = df[df['Consumption'] == 'Subutex'] # récupération des lignes où la colonne Subutex vaut 1
print(df_subutex)
