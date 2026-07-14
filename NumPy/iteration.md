# Notes d'apprentissage — `iteration.py`

> Convertir une image en **niveaux de gris** avec des **boucles Python imbriquées** — la méthode *lente* et pédagogique. À comparer avec `iteration_clean.py` (version vectorisée rapide).

## À quoi sert ce script

Il charge l'image d'exemple `flower.jpg`, la parcourt **pixel par pixel** avec deux boucles `for` imbriquées, calcule pour chaque pixel la moyenne de ses 3 canaux (Rouge, Vert, Bleu) — ce qui donne son niveau de gris — puis reconstruit l'image et l'affiche empilée au-dessus de l'originale.

C'est **volontairement inefficace** : le but est de montrer ce que la vectorisation NumPy permettra de faire en une seule ligne.

---

## Une image = un tableau NumPy 3D

Une image couleur est un tableau de forme `(hauteur, largeur, 3)` :
- les 2 premières dimensions = la position du pixel (ligne, colonne) ;
- la 3ᵉ dimension = les **3 canaux** de couleur R, V, B (valeurs de 0 à 255).

```python
flower.shape       # ex. (427, 640, 3)
flower[0, 0]       # le pixel en haut à gauche, ex. [ 2 19 13 ]  (R, V, B)
```

Le **niveau de gris** d'un pixel = la moyenne de ses 3 canaux. Gris clair ≈ 255, gris foncé ≈ 0.

---

## `load_sample_image('flower.jpg')`

Fonction de **scikit-learn** qui renvoie une image d'exemple sous forme de tableau NumPy `(H, L, 3)`. Pratique pour s'entraîner sans télécharger de fichier. L'autre image disponible est `'china.jpg'`.

```python
from sklearn.datasets import load_sample_image
img = load_sample_image('china.jpg')
```

---

## La double boucle (le cœur du script)

```python
output = []
for line in flower:          # parcourt chaque LIGNE de l'image
    for pixel in line:       # parcourt chaque PIXEL de la ligne
        moyenne = int(np.mean(pixel))         # moyenne des 3 canaux -> niveau de gris
        moyenne_3d = np.stack((moyenne, moyenne, moyenne))  # -> [g, g, g]
        output.append(moyenne_3d)
```

Ce que fait chaque étape :

### `np.mean(pixel)`
Moyenne des valeurs du pixel. `pixel = [200, 100, 60]` → `120.0`. `int(...)` la convertit en entier (les couleurs sont des entiers 0–255).

```python
np.mean([200, 100, 60])   # 120.0
```

### `np.stack((g, g, g))`
Assemble trois fois la valeur de gris pour reconstituer un pixel « RVB gris » `[g, g, g]`. Un pixel gris a ses 3 canaux **égaux**.

```python
np.stack((120, 120, 120))   # array([120, 120, 120])
```

> Pourquoi répéter la valeur ? Parce que `plt.imshow` attend une image à 3 canaux. Mettre la même valeur sur R, V et B produit un gris neutre.

---

## Reconstruction et affichage

### `np.array(output).reshape(flower.shape)`
`output` est une **liste plate** de tous les pixels. On la reconvertit en tableau puis on lui redonne la forme d'origine `(H, L, 3)` avec `reshape` (cf. `reshape.md`).

### `np.concatenate((img_black_and_white, flower), axis=0)`
Empile verticalement (cf. `concatenate.md`) l'image en gris **au-dessus** de l'originale pour les comparer côte à côte.

### `plt.imshow(...)` + `plt.show()`
- `imshow` prépare l'affichage d'un tableau comme une image.
- `show` ouvre la **fenêtre graphique** (bloquante : le script attend qu'on la ferme).

```python
import matplotlib.pyplot as plt
plt.imshow(img)   # dessine l'image
plt.show()        # affiche la fenêtre (ferme-la pour continuer)
```

---

## Pourquoi cette méthode est lente

Sur une image de ~430×640, la double boucle exécute **~275 000 itérations Python**, avec à chaque tour un appel de fonction (`np.mean`), un `np.stack` et un `append`. Chaque itération repasse par l'interpréteur Python.

`iteration_clean.py` fait exactement la même chose en **une instruction vectorisée** (`np.mean(flower, axis=2)`) exécutée en C — d'où un gain de temps énorme. C'est le **contraste central** du projet.

---

## À retenir

- Une image couleur est un tableau `(hauteur, largeur, 3)` ; un pixel est `[R, V, B]`.
- Niveau de gris = moyenne des 3 canaux ; un pixel gris a ses 3 canaux **égaux** (`[g, g, g]`).
- Boucler pixel par pixel **fonctionne mais est lent** : chaque itération coûte cher en Python.
- `plt.imshow` + `plt.show` affichent un tableau comme une image (fenêtre bloquante).
- La leçon : ce que fait cette double boucle, NumPy le fera en **une ligne** (voir `iteration_clean.md`).
