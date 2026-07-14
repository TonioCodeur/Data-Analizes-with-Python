# Notes d'apprentissage — `import_auto.py`

> Un **pipeline d'import/nettoyage** complet (lab IBM) : télécharger le jeu de données « automobile », lui donner des noms de colonnes, remplacer les valeurs manquantes, supprimer les lignes sans prix, puis résumer. Introduit la structure en **petites fonctions** + garde `__main__`.

## À quoi sert ce script

Il enchaîne les étapes classiques d'un projet de données :
1. **télécharger** le CSV depuis une URL IBM Skills Network ;
2. le **charger** dans un `DataFrame` ;
3. le **nettoyer** (colonnes nommées, `?` → `NaN`, lignes sans prix supprimées) ;
4. le **sauvegarder** nettoyé ;
5. en **afficher un résumé** (aperçu, types, stats, info).

C'est le patron de référence pour les scripts « pipeline » du projet (par opposition aux scripts « exploration »).

---

## L'architecture en fonctions

Chaque étape est une **petite fonction à responsabilité unique**, orchestrée par `import_automobile()`, le tout protégé par la garde `__main__` :

```python
def download_dataset(url, file_name): ...
def clean_dataset(df): ...
def summarize_dataset(df): ...
def import_automobile():           # orchestre les 3 précédentes
    ...
if __name__ == "__main__":
    import_automobile()
```

Avantages : code **lisible**, **testable**, et réutilisable (on peut importer `clean_dataset` ailleurs sans relancer le téléchargement).

---

## Les constantes de module

En haut du fichier, en `UPPER_SNAKE_CASE` (convention Python pour les constantes) :

```python
DATASET_URL = "https://.../auto.csv"     # source des données
OUTPUT_FILE_NAME = "auto_dataset.csv"    # fichier de sortie
COLUMN_HEADERS = ["symboling", "make", ..., "price"]   # noms des 26 colonnes
```

Le CSV brut d'IBM **n'a pas d'en-tête** : on fournit donc nous-mêmes la liste des noms de colonnes.

---

## Étape 1 — Télécharger : `urllib.request.urlretrieve`

Module de la **bibliothèque standard** (pas besoin d'installer quoi que ce soit) pour récupérer un fichier via HTTP.

### `urllib.request.urlretrieve(url, destination)`
Télécharge le contenu de `url` et l'enregistre dans le fichier `destination`.

```python
import urllib.request
urllib.request.urlretrieve("https://exemple.com/data.csv", "local.csv")
```

> En cas d'URL invalide ou de coupure réseau, cette fonction lève une exception. Les scripts du projet préfèrent transformer ce genre d'erreur en message clair (`raise SystemExit("...")`) plutôt qu'un long *traceback* — voir `../premieres_analyses_avec_pandas/import_data.md`.

---

## Étape 2 — Charger : `pd.read_csv(file, header=None)`

`header=None` indique que le fichier **n'a pas de ligne d'en-tête** : Pandas numérote les colonnes 0, 1, 2… On les renommera à l'étape suivante.

```python
df = pd.read_csv("auto_dataset.csv", header=None)
```

---

## Étape 3 — Nettoyer : `clean_dataset`

```python
def clean_dataset(df):
    df.columns = COLUMN_HEADERS          # (a) nommer les colonnes
    df = df.replace("?", np.nan)         # (b) marquer les valeurs manquantes
    return df.dropna(subset=["price"], axis=0)   # (c) supprimer les lignes sans prix
```

### (a) `df.columns = COLUMN_HEADERS`
Remplace les noms de colonnes par notre liste. Elle doit contenir **exactement** autant de noms que de colonnes.

### (b) `df.replace("?", np.nan)`
Dans ce jeu de données, les valeurs manquantes sont notées `"?"`. On les remplace par `np.nan` (le marqueur standard de « donnée manquante » que Pandas sait détecter et ignorer dans les calculs).

```python
df.replace("?", np.nan)              # un remplacement
df.replace({"?": np.nan, "-": np.nan})   # plusieurs marqueurs d'un coup
```

### (c) `df.dropna(subset=["price"], axis=0)`
Supprime les **lignes** (`axis=0`) qui ont un `NaN` dans la colonne `price`. `subset=[...]` limite la vérification à ces colonnes-là (une ligne sans prix est inutilisable pour une analyse de prix, mais on garde les lignes où d'autres champs manquent).

```python
df.dropna()                         # supprime toute ligne ayant AU MOINS un NaN
df.dropna(subset=["price"])         # supprime seulement si "price" est NaN
df.dropna(axis=1)                   # supprime les COLONNES contenant des NaN
df.dropna(how="all")                # supprime seulement les lignes entièrement vides
```

> Alternative fréquente au `dropna` : **remplir** les trous avec `df.fillna(valeur)` (ex. la moyenne de la colonne) plutôt que supprimer.

---

## Étape 4 — Sauvegarder : `df.to_csv(file, index=False)`

Écrit le `DataFrame` nettoyé dans un CSV. `index=False` **n'écrit pas** la colonne d'index de Pandas (0, 1, 2…), qui n'a pas de sens dans le fichier de sortie.

```python
df.to_csv("sortie.csv", index=False)     # sans la colonne d'index (recommandé ici)
df.to_csv("sortie.csv")                   # AVEC l'index -> colonne parasite
```

---

## Étape 5 — Résumer : `summarize_dataset`

Combine les méthodes d'inspection vues dans `../Pandas/dataframe.md` :

```python
print(df.head())                  # 5 premières lignes
print(df.dtypes)                  # type de chaque colonne
print(df.describe(include="all")) # stats de TOUTES les colonnes
df.info()                         # non-nuls, types, mémoire
```

- `df.head()` — aperçu.
- `df.dtypes` — utile pour repérer une colonne numérique restée en `object` (texte) à cause d'un `?`.
- `df.describe(include="all")` — inclut les colonnes texte (unique, top, freq) en plus des numériques.
- `df.info()` — révèle le nombre de valeurs manquantes par colonne.

---

## À retenir

- Un pipeline se découpe en **petites fonctions** (`download` / `clean` / `summarize`) orchestrées par une fonction principale sous `if __name__ == "__main__":`.
- `urllib.request.urlretrieve(url, fichier)` télécharge sans dépendance externe.
- `read_csv(..., header=None)` quand le CSV n'a pas d'en-tête → on nomme via `df.columns = [...]`.
- Nettoyage type : `replace("?", np.nan)` puis `dropna(subset=[...])` (ou `fillna`).
- `to_csv(..., index=False)` pour ne pas écrire l'index Pandas dans le fichier.
