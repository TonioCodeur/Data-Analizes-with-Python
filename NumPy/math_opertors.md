# Notes d'apprentissage — `math_opertors.py`

> Les **opérations mathématiques** sur les tableaux : scalaire, élément par élément, et la grande distinction entre `*` (Hadamard) et `@` (produit matriciel / scalaire).

> ℹ️ Le nom du fichier contient une coquille volontaire (`opertors` au lieu de `operators`) — elle est conservée telle quelle dans le projet.

## À quoi sert ce script

Il montre, sur des vecteurs et des matrices :
- la multiplication par un scalaire (`2 * arr`) ;
- la multiplication **élément par élément** (`arr1 * arr2`) ;
- l'addition ;
- l'opérateur `@` : **produit scalaire** entre vecteurs, **multiplication matricielle** entre matrices ;
- la reproductibilité avec `np.random.seed`, puis `np.concatenate`, `np.sum` et `.prod()`.

---

## Opérations élément par élément

Avec `+`, `-`, `*`, `/`, `**`, NumPy applique l'opération position par position. Les tableaux doivent avoir la même forme (ou être compatibles, cf. *broadcasting*).

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b     # [5 7 9]
a * b     # [ 4 10 18]   <- PAS un produit matriciel : juste 1*4, 2*5, 3*6
a ** 2    # [1 4 9]
b / a     # [4.  2.5 2. ]
```

Multiplier par un scalaire est un cas particulier (le nombre est « diffusé » sur tout le tableau) :

```python
2 * a     # [2 4 6]
```

> Le produit `a * b` s'appelle le **produit de Hadamard**. Ce n'est **pas** l'algèbre linéaire classique.

---

## Le broadcasting (bonus, très utile)

Quand les formes diffèrent, NumPy « étire » automatiquement la plus petite si c'est possible.

```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])       # forme (2, 3)
ligne = np.array([10, 20, 30])  # forme (3,)

m + ligne
# [[11 22 33]
#  [14 25 36]]   -> la ligne est ajoutée à chaque ligne de m
```

---

## L'opérateur `@` : produit scalaire et produit matriciel

`@` fait de l'**algèbre linéaire**, contrairement à `*`.

### Sur deux vecteurs → produit scalaire (un seul nombre)
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
a @ b        # 1*4 + 2*5 + 3*6 = 32
```
Équivalent à `np.dot(a, b)`.

### Sur deux matrices → multiplication matricielle
Règle des dimensions : `(m, n) @ (n, p) = (m, p)`. Le nombre de **colonnes** de la 1ʳᵉ doit égaler le nombre de **lignes** de la 2ᵉ.

```python
A = np.array([[1, 2],
              [3, 4]])          # (2, 2)
B = np.array([[5, 6],
              [7, 8]])          # (2, 2)

A @ B
# [[1*5+2*7  1*6+2*8]      [[19 22]
#  [3*5+4*7  3*6+4*8]]  =   [43 50]]
```

Différence à bien voir :
```python
A * B    # élément par élément : [[5 12] [21 32]]
A @ B    # produit matriciel   : [[19 22] [43 50]]
```

> **Piège des dimensions** : `np.ones((2, 3)) @ np.ones((2, 3))` lève une erreur (`3 ≠ 2`). Il faudrait `(2, 3) @ (3, k)`.

---

## Nombres aléatoires reproductibles

### `np.random.seed(n)`
Fixe la « graine » du générateur : la suite de nombres aléatoires devient **reproductible** (même graine → mêmes tirages). Indispensable pour des résultats vérifiables.

```python
np.random.seed(0)
np.random.randint(0, 10, size=3)   # toujours [5 0 3] avec la graine 0
```

### `np.random.randint(bas, haut, size=...)`
Entiers aléatoires dans `[bas, haut[` (borne haute **exclue**).

```python
np.random.randint(1, 7, size=(2, 2))   # simulation de dés, forme 2x2
```

Autres tirages fréquents :
```python
np.random.rand(3)            # 3 flottants dans [0, 1[
np.random.normal(0, 1, 5)    # 5 valeurs d'une loi normale (moyenne 0, écart-type 1)
np.random.choice([1, 2, 3])  # un élément au hasard dans une liste
```

---

## Réductions : `np.sum` et `.prod()`

```python
m = np.array([[1, 2], [3, 4]])

np.sum(m)      # 10   (somme de tous les éléments)
m.sum()        # 10   (méthode équivalente)
m.prod()       # 24   (produit : 1*2*3*4)
```

Comme pour `discover.md`, on peut réduire par axe :
```python
m.sum(axis=0)  # [4 6]  par colonne
m.sum(axis=1)  # [3 7]  par ligne
```

> ⚠️ `.prod()` peut vite dépasser la capacité des entiers (**overflow**) sur de grandes matrices. Le résultat peut alors « boucler » sur des valeurs négatives sans erreur.

---

## À retenir

- `*` = **élément par élément** (Hadamard) ; `@` = **algèbre linéaire** (produit scalaire / matriciel).
- Produit matriciel : `(m, n) @ (n, p) → (m, p)` — les dimensions intérieures doivent coïncider.
- `np.random.seed(n)` rend l'aléatoire **reproductible** ; `randint(bas, haut)` exclut la borne haute.
- `np.sum`, `.prod`, `.mean`… réduisent tout le tableau, ou par `axis`.
