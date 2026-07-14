# Notes d'apprentissage — `discover.py`

> Point d'entrée pour **découvrir NumPy** : créer un tableau, lire ses attributs, faire du calcul vectorisé et appliquer des fonctions universelles.

## À quoi sert ce script

Il crée un premier tableau 1D (un « vecteur »), affiche ses caractéristiques fondamentales (`dtype`, `ndim`, `shape`, `sum`, `mean`), montre la **vectorisation** (une opération s'applique à tout le tableau d'un coup), puis crée des matrices avec `np.ones`/`np.zeros`, en sélectionne une colonne, et termine par les **ufuncs** (`np.exp`, `np.cos`…) appliquées élément par élément.

L'idée centrale à retenir : en NumPy, **on ne fait presque jamais de boucle** — on manipule le tableau entier en une instruction.

---

## Le tableau NumPy (`ndarray`)

Un tableau NumPy est une grille d'éléments **tous du même type**, stockés de façon contiguë en mémoire. C'est ce qui le rend beaucoup plus rapide et compact qu'une liste Python.

### `np.array(objet)`
Convertit une liste (ou liste de listes) Python en tableau NumPy.

```python
import numpy as np

v = np.array([10, 20, 30])          # vecteur 1D
m = np.array([[1, 2], [3, 4]])      # matrice 2D (2 lignes, 2 colonnes)
```

---

## Les attributs d'un tableau

Ce sont des propriétés (sans parenthèses) qui décrivent le tableau.

| Attribut | Renvoie | Exemple sur `np.array([[1, 2, 3], [4, 5, 6]])` |
|---|---|---|
| `.dtype` | le type des éléments | `int64` |
| `.ndim` | le nombre de dimensions | `2` |
| `.shape` | la forme (tuple) | `(2, 3)` → 2 lignes, 3 colonnes |
| `.size` | le nombre total d'éléments | `6` |

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m.dtype)   # int64
print(m.ndim)    # 2
print(m.shape)   # (2, 3)
print(m.size)    # 6
```

> **Piège `shape`** : pour un vecteur, `shape` vaut `(3,)` et **pas** `(3)`. La virgule indique un tuple à un seul élément — c'est bien 1 dimension.

---

## Les méthodes de réduction : `.sum()` et `.mean()`

Une **réduction** transforme tout le tableau en un seul nombre (ou en un tableau plus petit).

```python
notes = np.array([12, 8, 15, 10])
print(notes.sum())    # 45  (somme)
print(notes.mean())   # 11.25 (moyenne)
print(notes.max())    # 15
print(notes.min())    # 8
```

Sur une matrice, on peut réduire **selon un axe** (voir aussi `concatenate.md`) :

```python
m = np.array([[1, 2], [3, 4]])
print(m.sum())          # 10  (tout)
print(m.sum(axis=0))    # [4 6]  (somme par colonne)
print(m.sum(axis=1))    # [3 7]  (somme par ligne)
```

---

## La vectorisation

Multiplier un tableau par un nombre applique l'opération à **chaque** élément, sans boucle. C'est le cœur de NumPy.

```python
prix = np.array([100, 200, 300])
prix_ttc = prix * 1.2        # [120. 240. 360.]
remise   = prix - 10         # [ 90 190 290]
```

Cela vaut aussi entre deux tableaux de même forme (élément par élément) :

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)   # [11 22 33]
```

---

## Créer des matrices « pré-remplies »

### `np.ones(shape)` et `np.zeros(shape)`
Créent une matrice de la forme demandée, remplie de `1.0` (ones) ou `0.0` (zeros). Le type par défaut est **flottant**.

```python
np.ones((2, 3))     # matrice 2x3 de 1.0
np.zeros((3,))      # vecteur de 3 zéros : [0. 0. 0.]
np.ones((2, 2), dtype=int)   # forcer des entiers : [[1 1] [1 1]]
```

À connaître dans la même famille :
```python
np.full((2, 2), 7)     # remplir avec une valeur au choix -> [[7 7] [7 7]]
np.arange(0, 10, 2)    # comme range : [0 2 4 6 8]
np.linspace(0, 1, 5)   # 5 valeurs régulières de 0 à 1 : [0. 0.25 0.5 0.75 1.]
```

---

## Le slicing (indexation par tranches)

`tableau[lignes, colonnes]`. Le `:` seul signifie « tout ».

```python
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

m[0]        # première ligne : [1 2 3]
m[:, 1]     # toute la colonne d'index 1 : [2 5 8]
m[1, 2]     # élément ligne 1, colonne 2 : 6
m[0:2, :]   # les 2 premières lignes
```

> Dans le script, `arr3[:, 5]` veut dire « toutes les lignes, colonne d'index 5 » (la 6ᵉ colonne, car on compte à partir de 0).

---

## Les fonctions universelles (ufuncs)

Une **ufunc** est une fonction NumPy qui s'applique automatiquement à chaque élément du tableau. Elles sont écrites en C : rapides et sans boucle Python.

```python
x = np.array([0.0, 1.0, 2.0])
np.exp(x)    # exponentielle : [1.    2.718 7.389]
np.sqrt(x)   # racine carrée : [0.    1.    1.414]
np.cos(x)    # cosinus
np.log(x)    # logarithme népérien (attention : log(0) = -inf)
```

> **Piège `np.log`** : `log(0)` renvoie `-inf` et déclenche un avertissement. Dans le script, `x` commence à `0.0`, donc `np.log(x)[0]` vaut `-inf` — c'est normal.

### `np.round(tableau, decimals=n)`
Arrondit chaque valeur à `n` décimales.

```python
np.round(np.array([3.14159, 2.71828]), decimals=2)   # [3.14 2.72]
```

---

## Les compréhensions de liste avec NumPy

Le script construit `x` avec `np.array([_/100 for _ in range(300)])`. C'est valide, mais on préfère en général la version NumPy native, plus rapide :

```python
x = np.arange(300) / 100      # équivalent : [0.   0.01 0.02 ... 2.99]
```

---

## À retenir

- Un `ndarray` contient **un seul type** d'éléments, décrit par `dtype` / `ndim` / `shape`.
- On **vectorise** : `arr * 2`, `a + b`, `np.exp(arr)` agissent sur tout le tableau, sans boucle.
- `np.zeros` / `np.ones` / `np.full` / `np.arange` / `np.linspace` créent des tableaux prêts à l'emploi.
- Le slicing `[:, k]` sélectionne des lignes/colonnes ; l'indexation commence à **0**.
- Les **ufuncs** (`exp`, `cos`, `log`, `round`…) s'appliquent élément par élément.
