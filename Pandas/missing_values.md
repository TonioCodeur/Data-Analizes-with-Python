# Notes d'apprentissage — `missing_values.py`

> Gérer les **valeurs manquantes** (NaN) avec Pandas : les **détecter**, comprendre les marqueurs non standard, puis comparer les deux grandes stratégies — **remplacer** (imputation par la moyenne / le mode) vs **supprimer** (`dropna`).

## À quoi sert ce script

Il charge un jeu de données immobilier « troué », en repère les valeurs manquantes, convertit les colonnes numériques, puis illustre **deux approches opposées** sur le même dataset :

- **Exemple 1** — combler les trous avec `.replace()` (moyenne pour les colonnes numériques, valeur la plus fréquente pour la colonne texte) ;
- **Exemple 2** — supprimer les lignes incomplètes avec `.dropna()`, sur une **copie** conservée intacte.

C'est un script d'**exploration** (code au niveau global, beaucoup de `print`), avec en plus une petite fonction de diagnostic `valeur_manquante`.

---

## Qu'est-ce qu'une « valeur manquante » ?

Une donnée absente est représentée par **`NaN`** (*Not a Number*) en Pandas. Les fonctions statistiques (`mean`, `sum`…) l'ignorent, et il faut la traiter avant beaucoup d'analyses (modèles, corrélations…).

Le piège : dans un fichier réel, une valeur manquante peut être écrite de **plein de façons différentes** : case vide, `NA`, `n/a`, `NaN`, `na`, `--`, `?`, `null`… Certaines sont reconnues automatiquement, d'autres non.

---

## Lire en déclarant les marqueurs manquants

### `pd.read_csv(link, na_values=['na', '--'])`
`pd.read_csv` reconnaît **déjà** par défaut une liste de marqueurs (`''`, `NA`, `n/a`, `NaN`, `NULL`, `None`…). Mais **pas** `na` en minuscules ni `--`. Le paramètre `na_values` **ajoute** nos propres marqueurs à cette liste par défaut.

```python
import pandas as pd
df = pd.read_csv("data.csv", na_values=["--", "na", "inconnu"])
# ces chaînes seront lues comme NaN, en plus des marqueurs standard
```

> **Pourquoi c'est crucial** : si `na` reste une chaîne de texte au lieu de devenir NaN, il « pollue » la colonne — celle-ci reste de type texte (`object`) et `isna()` ne le compte pas comme manquant.

---

## Détecter les valeurs manquantes

### `df[col].isna()`
Renvoie un masque booléen : `True` là où la valeur est manquante.

```python
s = pd.Series([1, None, 3])
s.isna()        # [False, True, False]
s.isna().sum()  # 1   (True compte pour 1 -> nombre de NaN)
```

### La fonction `valeur_manquante(df)` du script
Elle parcourt chaque colonne et affiche le nombre de NaN, colonne par colonne :

```python
def valeur_manquante(df):
    flag = 0
    for col in df.columns:
        if df[col].isna().sum() > 0:
            flag = 1
            print(f'"{col}": {df[col].isna().sum()} valeur(s) manquante(s)')
    if flag == 0:
        print("Le dataset ne contient plus de valeurs manquantes.")
```

Le `flag` sert de témoin : s'il reste à `0`, c'est qu'aucune colonne n'avait de NaN → message « propre ». C'est un **contrôle** pratique qu'on rappelle après chaque traitement.

> Équivalent vectorisé, sans boucle, pour aller vite :
> ```python
> df.isna().sum()          # nombre de NaN par colonne
> df.isna().sum().sum()    # nombre total de NaN dans tout le dataframe
> ```

### `df.info()`
Affiche pour chaque colonne son **type** et son **nombre de valeurs non nulles** — un moyen rapide de repérer les colonnes trouées et les colonnes restées en `object` par erreur.

---

## Reconvertir les colonnes numériques : `pd.to_numeric(..., errors='coerce')`

Quand une colonne numérique contient une valeur parasite (ici `HURLEY` dans `NUM_BATH`), Pandas lit **toute la colonne** comme du texte (`object`). On ne peut alors pas calculer sa moyenne.

`pd.to_numeric` la reconvertit ; `errors='coerce'` transforme en **NaN** tout ce qui n'est pas un nombre.

```python
import pandas as pd
s = pd.Series(["10", "20", "abc", "30"])
pd.to_numeric(s, errors="coerce")   # [10.0, 20.0, NaN, 30.0]
```

Dans le script :
```python
NUMERIC_COLUMNS = ['PID', 'ST_NUM', 'NUM_BEDROOMS', 'NUM_BATH', 'SQ_FT']
for col in NUMERIC_COLUMNS:
    df[col] = pd.to_numeric(df[col], errors='coerce')
```

Options de `errors` :
- `'raise'` (défaut) : lève une erreur si une valeur n'est pas convertible ;
- `'coerce'` : remplace les valeurs non convertibles par NaN (le choix ici) ;
- `'ignore'` : renvoie la colonne inchangée (déprécié).

---

## Copier un DataFrame : `df.copy()`

Pour pouvoir montrer les **deux** stratégies sur les mêmes données de départ, le script fige une copie **avant** de combler les trous :

```python
df_avec_na = df.copy()      # copie indépendante, qui garde encore les NaN
```

### Pourquoi `.copy()` est indispensable
Sans lui, `df2 = df` ne crée **pas** un nouveau tableau : les deux noms pointent vers le **même** objet. Modifier l'un modifierait l'autre.

```python
df2 = df            # même objet -> piège
df3 = df.copy()     # objet indépendant -> sûr
```

---

## Exemple 1 — REMPLACER avec `.replace()`

### `Series.replace(à_remplacer, valeur_de_remplacement)`
`replace` remplace des valeurs par d'autres. Ici on remplace `np.nan` par une valeur calculée.

```python
import numpy as np
for col in NUMERIC_COLUMNS:
    df[col] = df[col].replace(np.nan, df[col].mean())
```

`df[col].mean()` calcule la moyenne de la colonne (en ignorant les NaN), et chaque NaN est remplacé par cette moyenne. C'est l'**imputation par la moyenne**.

`replace` sait faire bien plus que remplacer des NaN :
```python
s.replace(0, 100)                  # remplace tous les 0 par 100
s.replace([1, 2], 0)               # remplace 1 ET 2 par 0
s.replace({"oui": 1, "non": 0})    # dictionnaire de correspondances
```

> **`replace` vs `fillna`** : pour combler **spécifiquement des NaN**, `fillna` est l'outil dédié et le plus idiomatique :
> ```python
> df[col] = df[col].fillna(df[col].mean())   # équivalent, plus lisible
> ```
> `replace(np.nan, x)` fonctionne, mais `replace` est surtout fait pour substituer des **valeurs quelconques**. Ce script illustre volontairement `replace` à titre pédagogique.

### La colonne catégorielle `OWN_OCCUPIED`
`OWN_OCCUPIED` contient du texte (`Y`/`N`) : une **moyenne n'a aucun sens**. On la remplit par sa valeur la plus fréquente, le **mode** :

```python
df['OWN_OCCUPIED'] = df['OWN_OCCUPIED'].replace(np.nan, df['OWN_OCCUPIED'].mode()[0])
```

`.mode()` renvoie une `Series` (il peut y avoir plusieurs valeurs ex æquo) ; `[0]` en prend la première.

```python
pd.Series(["Y", "N", "Y", "Y"]).mode()      # Series -> ['Y']
pd.Series(["Y", "N", "Y", "Y"]).mode()[0]   # 'Y'
```

> ⚠️ **Piège à connaître** : ne pas confondre `.mode()[0]` (valeur la plus fréquente) avec `.sum()[0]`. Sur une colonne texte, `.sum()` **concatène** toutes les chaînes (`'Y'+'N'+'N'+…` → `'YNN12YYYY'`) et `[0]` renverrait juste le **premier caractère** — ce n'est pas le mode. Pour imputer une colonne catégorielle, c'est bien `.mode()[0]` qu'il faut.

> **Note — ligne redondante** : le script réimpute ensuite `SQ_FT` séparément :
> ```python
> df['SQ_FT'] = df['SQ_FT'].replace(np.nan, df['SQ_FT'].mean())
> ```
> Cette ligne est **sans effet** : `SQ_FT` fait déjà partie de `NUMERIC_COLUMNS` et a donc déjà été rempli par la boucle juste au-dessus. À ce stade la colonne n'a plus aucun NaN, donc `replace` ne trouve rien à remplacer. On peut la supprimer sans rien changer au résultat.

---

## Exemple 2 — SUPPRIMER avec `.dropna()`

### `df.dropna()`
Supprime les **lignes** contenant au moins un NaN et renvoie un **nouveau** DataFrame.

```python
df_sans_na = df_avec_na.dropna()
```

Paramètres utiles :
```python
df.dropna()                       # supprime toute ligne ayant >= 1 NaN
df.dropna(axis=1)                 # supprime les COLONNES contenant des NaN
df.dropna(how="all")              # supprime seulement les lignes ENTIÈREMENT vides
df.dropna(subset=["price"])       # ne regarde que la colonne "price"
df.dropna(thresh=3)               # garde les lignes ayant au moins 3 valeurs non nulles
```

> **Résultat frappant ici** : sur ce jeu de 9 lignes, `dropna()` n'en garde qu'**une seule** — la seule ligne complète. Toutes les autres avaient au moins un trou. C'est la leçon centrale du script.

---

## Les deux stratégies en comparaison

| | `.replace()` / `.fillna()` (imputation) | `.dropna()` (suppression) |
|---|---|---|
| Effet | comble les trous | supprime les lignes trouées |
| Lignes conservées | **toutes** | seulement les complètes |
| Risque | introduit des valeurs « inventées » (moyenne) | **perte de données** massive si beaucoup de trous |
| Quand l'utiliser | peu de données, ou trous acceptables à estimer | beaucoup de données, trous rares |

Il n'y a pas de « bonne » réponse universelle : le choix dépend de la **proportion** de valeurs manquantes et de l'usage prévu des données.

---

## À retenir

- Une valeur manquante = **`NaN`** ; elle peut être écrite de multiples façons dans un fichier → `na_values=[...]` dans `read_csv` pour toutes les capturer.
- Détecter : `df[col].isna().sum()` par colonne, ou `df.isna().sum()` d'un coup.
- Une valeur parasite fait basculer une colonne en `object` → `pd.to_numeric(..., errors='coerce')` la re-typifie.
- `df.copy()` crée un DataFrame **indépendant** (ne pas confondre avec `df2 = df`).
- **Imputer** : `replace(np.nan, x)` ou, mieux, `fillna(x)` — moyenne pour le numérique, **mode** (`.mode()[0]`) pour le catégoriel.
- **Supprimer** : `dropna()` — simple mais potentiellement très destructeur.
