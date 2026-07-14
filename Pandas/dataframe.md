# Notes d'apprentissage — `dataframe.py`

> Premiers pas avec **Pandas** : charger un CSV dans un `DataFrame`, l'**inspecter** (`head`, `describe`, `info`…), **sélectionner des lignes** avec `.loc`, et **filtrer** avec un masque booléen.

## À quoi sert ce script

Il lit le fichier `drugs_consumption.csv` dans un `DataFrame`, en affiche plusieurs aperçus, récupère des lignes par leur index avec `.loc`, puis extrait toutes les lignes où la colonne `Consumption` vaut `'Subutex'`.

---

## Les deux objets de base de Pandas

- **`Series`** : une colonne (un tableau 1D **étiqueté** par un index).
- **`DataFrame`** : un tableau 2D = un ensemble de `Series` partageant le même index. C'est l'équivalent d'une feuille de calcul (lignes × colonnes nommées).

```python
import pandas as pd
s = pd.Series([10, 20, 30], name="age")
df = pd.DataFrame({"nom": ["Ana", "Bob"], "age": [30, 25]})
```

---

## Charger des données : `pd.read_csv`

### `pd.read_csv(chemin, sep=',', header=0)`
Lit un fichier CSV et renvoie un `DataFrame`.

- `sep=','` : le séparateur de colonnes (`;` ou `\t` selon les fichiers).
- `header=0` : la **ligne 0 contient les noms de colonnes**. (`header=None` = pas d'en-tête, Pandas numérote alors les colonnes 0, 1, 2… — c'est ce que font les scripts du dossier `lab_data_importation/`.)

```python
df = pd.read_csv("ventes.csv", sep=";", header=0)
```

> Le script construit le chemin avec `Path(__file__).parent / 'drugs_consumption.csv'` : cela pointe vers le CSV **situé à côté du script**, quel que soit le dossier depuis lequel on lance Python. Plus robuste qu'un chemin relatif « en dur ».

---

## Inspecter un DataFrame

| Appel | Ce qu'il montre |
|---|---|
| `df.head(n)` | les `n` premières lignes (5 par défaut) |
| `df.tail(n)` | les `n` dernières lignes |
| `df.sample(n)` | `n` lignes tirées **au hasard** |
| `df.describe()` | statistiques des colonnes numériques (count, mean, std, min, quartiles, max) |
| `df.describe(include='all')` | statistiques de **toutes** les colonnes (y compris texte : unique, top, freq) |
| `df.info()` | types de colonnes, nombre de valeurs non nulles, mémoire |
| `df.shape` | `(nb_lignes, nb_colonnes)` |
| `df.columns` | la liste des noms de colonnes |
| `df.dtypes` | le type de chaque colonne |

```python
df.head()               # aperçu rapide
df.describe()           # résumé chiffré
df.info()               # santé des données (valeurs manquantes ?)
```

> **Piège `df.info()`** : cette méthode **affiche** directement et renvoie `None`. Faire `print(df.info())` affiche l'info **puis** un `None` superflu — dans le script c'est sans conséquence, mais il suffit d'écrire `df.info()`.

---

## Sélectionner des lignes : `.loc`

`.loc` sélectionne par **étiquette** d'index (le « nom » de la ligne). Avec l'index par défaut (0, 1, 2…), l'étiquette est le numéro de ligne.

```python
df.loc[5]          # la ligne d'index 5 (renvoie une Series)
df.loc[5:10]       # les lignes 5 à 10 INCLUSES  (⚠ borne de fin incluse)
df.loc[:]          # toutes les lignes
```

> **Différence cruciale `.loc` vs `.iloc`** :
> - `.loc[5:10]` sélectionne par **étiquette**, borne de fin **incluse** → lignes 5,6,7,8,9,10.
> - `.iloc[5:10]` sélectionne par **position**, borne de fin **exclue** (comme les listes Python) → lignes 5,6,7,8,9.

### Sélectionner lignes ET colonnes
```python
df.loc[5, "age"]                 # valeur : ligne 5, colonne "age"
df.loc[5:10, ["nom", "age"]]     # lignes 5-10, colonnes choisies
df.loc[:, "age"]                 # toute la colonne "age"
```

---

## Sélectionner des colonnes

```python
df["Consumption"]              # une colonne -> Series
df[["Consumption", "nom"]]     # plusieurs colonnes -> DataFrame (double crochet !)
```

---

## Filtrer avec un masque booléen

Comme en NumPy (cf. `../NumPy/reshape.md`), une comparaison sur une colonne crée un masque de `True`/`False`, qu'on passe entre crochets pour ne garder que les lignes correspondantes.

```python
# toutes les lignes où Consumption vaut 'Subutex'
df_subutex = df[df['Consumption'] == 'Subutex']
```

Étape par étape :
```python
masque = df['Consumption'] == 'Subutex'   # Series de True/False
df[masque]                                 # ne garde que les lignes True
```

### Conditions multiples
On combine avec `&` (et), `|` (ou), `~` (non), **chaque condition entre parenthèses** :

```python
df[(df['age'] > 18) & (df['age'] < 65)]    # entre 18 et 65
df[(df['ville'] == 'Paris') | (df['ville'] == 'Lyon')]
```

Autre méthode lisible pour « appartient à une liste » :
```python
df[df['ville'].isin(['Paris', 'Lyon'])]
```

> **Piège** : sur un DataFrame aussi, on utilise `&`/`|` et **pas** `and`/`or`, et on **parenthèse** chaque condition.

---

## À retenir

- `pd.read_csv(chemin, sep=..., header=...)` charge un CSV ; `header=0` = 1ʳᵉ ligne = noms de colonnes.
- Inspecter : `head`, `tail`, `sample`, `describe(include='all')`, `info`, `shape`, `dtypes`.
- `.loc` = sélection par **étiquette**, borne de fin **incluse** ; `.iloc` = par **position**, borne **exclue**.
- Une colonne se prend avec `df["col"]` ; plusieurs avec `df[["a", "b"]]` (double crochet).
- Filtrer = masque booléen : `df[df['col'] == valeur]`, conditions combinées avec `&`/`|` parenthésées.
