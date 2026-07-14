# NumPy — Apprentissage / Learning

> **FR :** Ce dossier regroupe une série de petits scripts d'apprentissage de **NumPy** (calcul numérique en Python) et de son utilisation pour le traitement d'images. Chaque script illustre une notion précise.
>
> **EN:** This folder gathers a series of small scripts for learning **NumPy** (numerical computing in Python) and using it for image processing. Each script illustrates one specific concept.

---

## Sommaire / Table of contents

| Fichier / File | Notion / Concept |
|---|---|
| [`discover.py`](discover.py) | Découverte de NumPy / Getting started |
| [`concatenate.py`](concatenate.py) | Concaténation de matrices / Concatenating matrices |
| [`math_opertors.py`](math_opertors.py) | Opérateurs mathématiques / Math operators |
| [`reshape.py`](reshape.py) | Redimensionnement & masques / Reshaping & masking |
| [`iteration.py`](iteration.py) | Niveaux de gris par boucles / Grayscale via loops |
| [`iteration_clean.py`](iteration_clean.py) | Niveaux de gris vectorisé / Vectorized grayscale |

---

## Prérequis / Requirements

**FR :** Il faut Python 3 et les bibliothèques suivantes (un environnement virtuel `venv/` est présent dans le dossier).
**EN:** You need Python 3 and the following libraries (a virtual environment `venv/` is present in the folder).

- **numpy** — EN: arrays and numerical computation. / FR: tableaux et calcul numérique.
- **matplotlib** — EN: displaying images/plots. / FR: affichage d'images/graphiques.
- **scikit-learn** — EN: provides the sample image `flower.jpg`. / FR: fournit l'image d'exemple `flower.jpg`.

### Installation avec `requirements.txt` / Installing with `requirements.txt`

**FR :** Toutes les dépendances (et leurs versions) sont listées dans [`requirements.txt`](requirements.txt). Pour les installer d'un coup :
**EN:** All dependencies (and their versions) are listed in [`requirements.txt`](requirements.txt). To install them all at once:

```bash
pip install -r requirements.txt
```

**FR :** *(Recommandé)* Créez et activez d'abord un environnement virtuel pour isoler les dépendances du projet :
**EN:** *(Recommended)* First create and activate a virtual environment to isolate the project dependencies:

```bash
# 1. Créer / Create
python -m venv venv

# 2a. Activer sous Windows (PowerShell) / Activate on Windows (PowerShell)
venv\Scripts\Activate.ps1
# 2b. Activer sous macOS / Linux / Activate on macOS / Linux
source venv/bin/activate

# 3. Installer les dépendances / Install the dependencies
pip install -r requirements.txt
```

---

## Description fichier par fichier / File-by-file description

### 1. `discover.py`

**FR :** Point d'entrée pour découvrir NumPy. Il crée un tableau 1D et affiche ses attributs fondamentaux : version de NumPy, type (`dtype`), nombre de dimensions (`ndim`), forme (`shape`), somme et moyenne. Il montre la **vectorisation** (`arr * 2`), la création de matrices avec `np.ones` et `np.zeros`, le **slicing** de colonnes (`arr3[:, 5]`) et les **fonctions universelles** (`np.exp`, `np.cos`, `np.sin`, `np.log`, `np.round`) qui s'appliquent à chaque élément.

**EN:** Entry point to discover NumPy. It creates a 1D array and prints its fundamental attributes: NumPy version, type (`dtype`), number of dimensions (`ndim`), shape (`shape`), sum and mean. It demonstrates **vectorization** (`arr * 2`), matrix creation with `np.ones` and `np.zeros`, column **slicing** (`arr3[:, 5]`), and **universal functions** (`np.exp`, `np.cos`, `np.sin`, `np.log`, `np.round`) that apply element-wise.

### 2. `concatenate.py`

**FR :** Illustre `np.concatenate`. On assemble deux matrices `zeros` et `ones` : avec `axis=0` (empilement vertical, forme `(4, 3)`) et avec `axis=1` (accolage horizontal, forme `(2, 6)`). Notion clé : l'**axe** détermine la direction de l'assemblage.

**EN:** Demonstrates `np.concatenate`. Two matrices `zeros` and `ones` are joined: with `axis=0` (vertical stacking, shape `(4, 3)`) and with `axis=1` (horizontal joining, shape `(2, 6)`). Key idea: the **axis** controls the direction of the join.

### 3. `math_opertors.py`

**FR :** Montre les opérations mathématiques sur les tableaux : multiplication par un scalaire (`2 * arr1`), produit **élément par élément** (`arr1 * arr2`), addition, et l'opérateur `@` qui donne le **produit scalaire** entre deux vecteurs et la **multiplication matricielle** entre deux matrices. Utilise `np.random.seed` pour la **reproductibilité**, puis `np.concatenate`, `np.sum` et `.prod()`.

**EN:** Shows math operations on arrays: scalar multiplication (`2 * arr1`), **element-wise** product (`arr1 * arr2`), addition, and the `@` operator which gives the **dot product** between two vectors and **matrix multiplication** between two matrices. Uses `np.random.seed` for **reproducibility**, then `np.concatenate`, `np.sum` and `.prod()`.

> ⚠️ **FR :** Le commentaire d'origine indiquait qu'`arr1 @ arr2` provoquerait une erreur — c'est faux : sur deux vecteurs, `@` calcule bien le produit scalaire (le commentaire a été corrigé).
> ⚠️ **EN:** The original comment said `arr1 @ arr2` would raise an error — that is incorrect: on two vectors, `@` computes the dot product (the comment has been fixed).

### 4. `reshape.py`

**FR :** Illustre `.reshape()` pour réorganiser un tableau sans changer ses données (1D → 3x3 → 1x9), à condition que le **nombre total d'éléments soit conservé**. Montre aussi les **masques booléens** : `matrix_random[matrix_random <= 17] = 0` remplace par 0, en une seule opération vectorisée, toutes les valeurs ≤ 17.

**EN:** Demonstrates `.reshape()` to reorganize an array without changing its data (1D → 3x3 → 1x9), as long as the **total number of elements is preserved**. Also shows **boolean masking**: `matrix_random[matrix_random <= 17] = 0` replaces with 0, in a single vectorized operation, every value ≤ 17.

> **Note — FR :** `import random as rd` est présent mais inutilisé. **EN:** `import random as rd` is present but unused.

### 5. `iteration.py`

**FR :** Applique NumPy au **traitement d'image**. On charge `flower.jpg`, puis on la convertit en niveaux de gris avec des **boucles imbriquées** (parcours pixel par pixel) : pour chaque pixel, on calcule la moyenne des 3 canaux RVB. C'est la méthode **lente** (pédagogique). Le résultat est affiché au-dessus de l'image originale avec `np.concatenate` et `plt.imshow`.

**EN:** Applies NumPy to **image processing**. It loads `flower.jpg`, then converts it to grayscale using **nested loops** (pixel-by-pixel traversal): for each pixel, it averages the 3 RGB channels. This is the **slow** (educational) method. The result is displayed above the original image with `np.concatenate` and `plt.imshow`.

### 6. `iteration_clean.py`

**FR :** Même objectif que `iteration.py`, mais en version **vectorisée** et rapide. `np.mean(flower, axis=2)` calcule la moyenne des canaux en une seule instruction, sans boucle, puis `np.repeat` + `reshape` reconstruisent une image RVB. C'est le **contraste clé** du projet : boucles Python (lent) vs vectorisation NumPy (rapide).

**EN:** Same goal as `iteration.py`, but in a **vectorized** and fast version. `np.mean(flower, axis=2)` averages the channels in a single instruction, with no loop, then `np.repeat` + `reshape` rebuild an RGB image. This is the project's **key contrast**: Python loops (slow) vs NumPy vectorization (fast).

---

## Comment exécuter / How to run

```bash
python discover.py
python concatenate.py
python math_opertors.py
python reshape.py
python iteration.py        # ouvre une fenêtre image / opens an image window
python iteration_clean.py  # ouvre une fenêtre image / opens an image window
```

---

## Synthèse — ce que ce projet apprend / Summary — what this project teaches

**FR :**
1. **Création de tableaux** : `np.array`, `np.zeros`, `np.ones`, `np.random.randint`, compréhensions de listes.
2. **Attributs d'un tableau** : `dtype`, `ndim`, `shape`, et méthodes `sum`, `mean`, `prod`.
3. **Vectorisation** : les opérations (`+`, `*`, ufuncs `np.exp`, `np.cos`…) s'appliquent à tout le tableau sans boucle.
4. **Algèbre** : différence entre produit élément par élément (`*`) et produit matriciel / scalaire (`@`).
5. **Formes** : `reshape` (nombre d'éléments conservé) et `concatenate` (assemblage selon un `axis`).
6. **Indexation** : slicing (`[:, 5]`) et masques booléens pour modifier des sous-ensembles.
7. **Reproductibilité** : `np.random.seed`.
8. **Application concrète** : une image est un tableau NumPy 3D ; on la transforme en niveaux de gris, et on compare l'approche par **boucles** à l'approche **vectorisée** (bien plus rapide).

**EN:**
1. **Creating arrays**: `np.array`, `np.zeros`, `np.ones`, `np.random.randint`, list comprehensions.
2. **Array attributes**: `dtype`, `ndim`, `shape`, and the `sum`, `mean`, `prod` methods.
3. **Vectorization**: operations (`+`, `*`, ufuncs `np.exp`, `np.cos`…) apply to the whole array with no loop.
4. **Algebra**: difference between the element-wise product (`*`) and the matrix / dot product (`@`).
5. **Shapes**: `reshape` (element count preserved) and `concatenate` (joining along an `axis`).
6. **Indexing**: slicing (`[:, 5]`) and boolean masks to modify subsets.
7. **Reproducibility**: `np.random.seed`.
8. **Concrete application**: an image is a 3D NumPy array; we turn it into grayscale, and compare the **loop-based** approach with the **vectorized** one (much faster).
