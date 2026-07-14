# Notes d'apprentissage — `reshape.py`

> **Redimensionner** un tableau avec `.reshape()` (sans changer les données) et modifier des sous-ensembles avec les **masques booléens**.

## À quoi sert ce script

Il crée un vecteur des entiers 1..9, le transforme en matrice 3×3 puis en ligne 1×9, montre qu'une matrice 5×4 peut devenir 2×10 (car 20 = 20), puis génère une matrice 10×10 aléatoire et met à `0` toutes les valeurs ≤ 17 via un **masque booléen**.

---

## `.reshape(nouvelle_forme)`

Réorganise les éléments d'un tableau dans une nouvelle forme, **sans changer les données ni leur ordre**.

**Règle d'or** : le nombre total d'éléments doit être **conservé**. `3×3 = 9`, `1×9 = 9`, `2×10 = 5×4 = 20`.

```python
import numpy as np

v = np.arange(1, 13)        # [1 2 ... 12], 12 éléments
v.reshape((3, 4))           # 3 lignes, 4 colonnes  (3*4 = 12  ✓)
v.reshape((2, 6))           # 2 lignes, 6 colonnes  (2*6 = 12  ✓)
v.reshape((5, 5))           # ERREUR : 25 ≠ 12
```

### L'astuce `-1` (dimension automatique)
`-1` demande à NumPy de **calculer** la dimension manquante.

```python
v = np.arange(12)
v.reshape((3, -1))    # NumPy déduit 4 colonnes -> (3, 4)
v.reshape((-1, 2))    # NumPy déduit 6 lignes   -> (6, 2)
v.reshape(-1)         # remet à plat en 1D       -> (12,)
```

### `reshape` vs `flatten` / `ravel`
```python
m = np.array([[1, 2], [3, 4]])
m.flatten()   # [1 2 3 4]  (copie aplatie)
m.ravel()     # [1 2 3 4]  (vue si possible, plus économe)
```

> **Ordre de remplissage** : par défaut NumPy lit/écrit ligne par ligne (ordre « C »). `reshape` ne mélange pas les données, il les regroupe simplement différemment.

---

## Les masques booléens

Une **comparaison** sur un tableau produit un tableau de `True`/`False` de même forme. Ce masque sert ensuite à **sélectionner ou modifier** des éléments.

### Étape 1 — créer le masque
```python
notes = np.array([12, 8, 15, 4, 18])
masque = notes >= 10       # [ True False  True False  True]
```

### Étape 2 — filtrer avec le masque
```python
notes[masque]              # [12 15 18]  (uniquement les True)
notes[notes >= 10]         # idem, en une ligne
```

### Étape 3 — modifier via le masque
C'est ce que fait le script (`matrix_random[matrix_random <= 17] = 0`) :

```python
notes[notes < 10] = 0      # met à 0 toutes les notes < 10
# notes -> [12  0 15  0 18]
```

### Combiner plusieurs conditions
On utilise `&` (et), `|` (ou), `~` (non), **avec des parenthèses** autour de chaque condition.

```python
m = np.arange(20)
m[(m > 5) & (m < 15)]      # valeurs strictement entre 5 et 15
m[(m < 3) | (m > 17)]      # valeurs < 3 OU > 17
```

> **Piège** : ne pas utiliser `and`/`or` (mots-clés Python) sur des tableaux — ils lèvent une erreur. Il faut `&`/`|`. Et toujours **parenthéser** : `m > 5 & m < 15` est mal interprété à cause de la priorité des opérateurs.

---

## Fonctions apparentées utiles

```python
np.where(notes >= 10, "reçu", "recalé")   # choisit selon la condition, élément par élément
np.any(notes >= 10)     # True s'il existe au moins une valeur qui satisfait la condition
np.all(notes >= 10)     # True si TOUTES la satisfont
np.count_nonzero(notes >= 10)   # compte combien de True
```

---

## Note sur le script

`import random as rd` (module standard de Python) est présent mais **jamais utilisé** : les tirages aléatoires viennent de `np.random`. C'est un import superflu.

---

## À retenir

- `.reshape()` change la **forme** mais pas les données ; le **nombre d'éléments doit être conservé**.
- `-1` laisse NumPy **déduire** une dimension ; `reshape(-1)` remet à plat.
- Une comparaison (`arr <= 17`) crée un **masque booléen** qui filtre (`arr[masque]`) ou modifie (`arr[masque] = 0`).
- On combine les conditions avec `&`, `|`, `~` **entre parenthèses** — jamais `and`/`or`.
