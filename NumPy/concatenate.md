# Notes d'apprentissage — `concatenate.py`

> Comment **assembler deux matrices** avec `np.concatenate`, et comprendre la notion cruciale d'**axe** (`axis`).

## À quoi sert ce script

Il crée deux matrices 2×3 (`zeros` et `ones`) et les colle ensemble de deux façons :
- `axis=0` → empilement **vertical** (l'une sous l'autre) → forme `(4, 3)` ;
- `axis=1` → accolage **horizontal** (côte à côte) → forme `(2, 6)`.

La leçon clé : **l'axe détermine la direction de l'assemblage**.

---

## Comprendre les axes

Pour une matrice 2D :
- `axis=0` = l'axe des **lignes** (vertical, on descend). Concaténer sur `axis=0` **ajoute des lignes**.
- `axis=1` = l'axe des **colonnes** (horizontal, on va à droite). Concaténer sur `axis=1` **ajoute des colonnes**.

```
axis=0  ↓ (lignes)
axis=1  → (colonnes)
```

Moyen mnémotechnique : `axis=0` agit sur la **première** dimension de `shape` (le nombre de lignes), `axis=1` sur la **deuxième** (le nombre de colonnes).

---

## `np.concatenate((a, b, ...), axis=...)`

Assemble une séquence de tableaux le long d'un axe existant.

**Règle absolue** : toutes les dimensions doivent correspondre, **sauf** celle de l'axe de concaténation.

### Exemple vertical (`axis=0`)
Les deux matrices doivent avoir le **même nombre de colonnes**.

```python
import numpy as np

a = np.array([[1, 1, 1]])          # forme (1, 3)
b = np.array([[2, 2, 2],
              [3, 3, 3]])          # forme (2, 3)

np.concatenate((a, b), axis=0)
# [[1 1 1]
#  [2 2 2]
#  [3 3 3]]   -> forme (3, 3)
```

### Exemple horizontal (`axis=1`)
Les deux matrices doivent avoir le **même nombre de lignes**.

```python
a = np.array([[1], [2]])           # forme (2, 1)
b = np.array([[7, 8], [9, 0]])     # forme (2, 2)

np.concatenate((a, b), axis=1)
# [[1 7 8]
#  [2 9 0]]   -> forme (2, 3)
```

### Erreur classique
```python
a = np.zeros((2, 3))
b = np.ones((2, 4))
np.concatenate((a, b), axis=0)     # ERREUR : 3 colonnes vs 4 colonnes
np.concatenate((a, b), axis=1)     # OK : mêmes 2 lignes -> forme (2, 7)
```

---

## Les raccourcis utiles

NumPy propose des fonctions plus lisibles pour les cas courants :

```python
np.vstack((a, b))    # empilement vertical   = concatenate(axis=0)
np.hstack((a, b))    # accolage horizontal   = concatenate(axis=1)
np.stack((a, b))     # crée un NOUVEL axe (empile en 3D)
```

Différence importante entre `concatenate` et `stack` :
- `concatenate` fusionne le long d'un axe **existant** (le nombre de dimensions ne change pas).
- `stack` ajoute une **nouvelle** dimension.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.concatenate((a, b))   # [1 2 3 4 5 6]      -> forme (6,)  (reste 1D)
np.stack((a, b))         # [[1 2 3] [4 5 6]]  -> forme (2, 3) (devient 2D)
```

---

## À retenir

- `np.concatenate((a, b), axis=...)` colle des tableaux **le long d'un axe existant**.
- `axis=0` = vertical (ajoute des lignes) ; `axis=1` = horizontal (ajoute des colonnes).
- Toutes les dimensions doivent coïncider **sauf** celle de l'axe choisi.
- `vstack`/`hstack` sont des raccourcis lisibles ; `stack` crée une **nouvelle** dimension.
