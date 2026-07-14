# Notes d'apprentissage — `iteration_clean.py`

> La **version vectorisée** de `iteration.py` : convertir une image en niveaux de gris en **une seule instruction NumPy**, sans aucune boucle. C'est la « bonne » façon de faire.

## À quoi sert ce script

Même objectif que `iteration.py` (mettre `flower.jpg` en niveaux de gris), mais :
- au lieu de deux boucles `for` sur ~275 000 pixels,
- on écrit **`np.mean(flower, axis=2)`** qui calcule la moyenne des 3 canaux pour tous les pixels **d'un coup**.

C'est le cœur pédagogique du projet : **boucles Python (lent) vs vectorisation NumPy (rapide)**.

---

## `np.mean(flower, axis=2)` — la ligne magique

L'image a la forme `(hauteur, largeur, 3)`. L'`axis=2` est celui des **canaux de couleur** (R, V, B).

Faire la moyenne **le long de l'axe 2**, c'est réduire les 3 canaux de chaque pixel à une seule valeur → une image `(hauteur, largeur)` en niveaux de gris.

```python
import numpy as np

pixel = np.array([[[200, 100, 60],   # 1 ligne, 2 pixels, 3 canaux
                   [ 30,  30, 30]]])  # forme (1, 2, 3)

np.mean(pixel, axis=2)
# [[120.  30.]]   -> forme (1, 2) : un niveau de gris par pixel
```

Comparaison des axes sur la même image :

| Appel | Réduit selon | Résultat |
|---|---|---|
| `np.mean(flower)` | tout | un seul nombre |
| `np.mean(flower, axis=0)` | les lignes | forme `(largeur, 3)` |
| `np.mean(flower, axis=2)` | **les canaux** | forme `(hauteur, largeur)` ✅ |

Le paramètre `dtype=int` force le résultat en entiers (les couleurs vont de 0 à 255).

> **L'idée générale** : `axis=k` signifie « effectue la réduction en faisant disparaître la dimension `k` ». Ici on fait disparaître l'axe des couleurs.

---

## `np.repeat(moyenne, 3)` — reconstituer 3 canaux

Après la moyenne, chaque pixel n'a qu'**une** valeur de gris. Pour l'afficher, `plt.imshow` veut de nouveau 3 canaux `[g, g, g]`. `np.repeat` duplique chaque valeur.

```python
np.repeat([5, 6, 7], 3)      # [5 5 5 6 6 6 7 7 7]
```

Puis `.reshape(flower.shape)` regroupe ces valeurs répétées dans la forme `(H, L, 3)` d'origine (cf. `reshape.md`).

```python
img_np = np.repeat(moyenne, 3).reshape(flower.shape)
```

> **Nuance `repeat` vs `tile`** :
> ```python
> np.repeat([1, 2], 3)   # [1 1 1 2 2 2]  (répète chaque élément)
> np.tile([1, 2], 3)     # [1 2 1 2 1 2]  (répète le motif entier)
> ```
> Ici `repeat` est le bon choix : on veut `[g, g, g]` par pixel, pas une répétition du motif.

---

## `np.concatenate(..., axis=0)` + affichage

Comme dans `iteration.py`, on empile l'image grise **au-dessus** de l'originale (`axis=0`, cf. `concatenate.md`) puis on affiche avec `plt.imshow` / `plt.show` (fenêtre bloquante).

---

## Le gain : pourquoi la vectorisation est rapide

| | `iteration.py` | `iteration_clean.py` |
|---|---|---|
| Méthode | 2 boucles `for` imbriquées | 1 appel `np.mean(..., axis=2)` |
| Nombre d'itérations Python | ~275 000 | **0** |
| Où tourne le calcul | interpréteur Python | code C compilé de NumPy |
| Vitesse | lent | **beaucoup plus rapide** |

La boucle Python paie, à chaque pixel, le coût de l'interpréteur. La version vectorisée délègue toute la boucle au code C interne de NumPy, qui traite le tableau en bloc. C'est exactement l'enseignement mesuré par `perf.py` et `test_perf_numpy.py`.

---

## À retenir

- **Vectoriser** = remplacer une boucle par une opération sur le tableau entier. Ici : `np.mean(flower, axis=2)`.
- `axis=k` réduit (fait disparaître) la dimension `k` ; l'axe 2 d'une image = ses canaux de couleur.
- `np.repeat` duplique **chaque élément** ; `np.tile` répète le **motif entier**.
- Même résultat que les boucles, mais exécuté en C → gain de vitesse majeur.
