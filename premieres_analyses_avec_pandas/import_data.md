# Notes d'apprentissage — `import_data.py`

> Un **premier import** minimaliste avec Pandas : créer un dossier de sortie, télécharger un CSV, gérer proprement une erreur de téléchargement, puis sauvegarder. Introduit `pathlib.Path` et la gestion d'erreurs `try/except` + `raise SystemExit`.

## À quoi sert ce script

C'est la version la plus simple du pipeline d'import du projet (sans fonctions ni nettoyage) :
1. préparer le chemin de sortie `data/automobile.csv` (et créer le dossier `data/` si besoin) ;
2. télécharger le CSV directement avec `pd.read_csv(URL)` ;
3. si le téléchargement échoue, **arrêter proprement** avec un message clair ;
4. sauvegarder le fichier sans l'index Pandas.

---

## Gérer les chemins avec `pathlib.Path`

`Path` (bibliothèque standard) représente un chemin de fichier de façon portable (Windows/Mac/Linux) et lisible.

### Construire un chemin avec `/`
L'opérateur `/` assemble les morceaux d'un chemin, quel que soit le système :

```python
from pathlib import Path
chemin = Path("data") / "automobile.csv"    # data/automobile.csv (ou data\automobile.csv sous Windows)
```

### `.parent`
Renvoie le dossier **contenant** le fichier.

```python
Path("data/automobile.csv").parent          # -> Path("data")
```

### `.mkdir(parents=True, exist_ok=True)`
Crée le dossier.
- `parents=True` : crée aussi les dossiers intermédiaires manquants (`a/b/c`).
- `exist_ok=True` : ne lève **pas** d'erreur si le dossier existe déjà.

```python
OUTPUT_PATH = Path("data/automobile.csv")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)   # garantit que data/ existe
```

> Sans `exist_ok=True`, relancer le script une 2ᵉ fois planterait car `data/` existerait déjà.

---

## Télécharger directement avec `pd.read_csv(URL)`

Pandas sait lire une URL comme un fichier local : il **télécharge et parse** en une étape.

```python
df = pd.read_csv(URL, header=None, na_values="?")
```

Paramètres utilisés :
- `header=None` : le CSV n'a pas de ligne d'en-tête (colonnes numérotées 0, 1, 2…).
- `na_values="?"` : traite directement `?` comme une **valeur manquante** (`NaN`) **dès la lecture**. Plus concis que le `df.replace("?", np.nan)` fait après coup dans les scripts de `../lab_data_importation/`.

```python
# equivalents :
pd.read_csv(url, na_values="?")          # marque ? en NaN à la lecture
# ... vs ...
df = pd.read_csv(url); df.replace("?", np.nan)   # même effet, en 2 temps
```

> ⚠️ **L'URL du script est erronée** (`https://archive.ics.edu/...` n'existe pas ; l'archive UCI réelle est `archive.ics.uci.edu`). Le téléchargement échouera donc — ce qui est justement l'occasion de voir la gestion d'erreur ci-dessous fonctionner.

---

## Gérer une erreur proprement : `try` / `except` + `raise SystemExit`

Un téléchargement peut échouer (URL fausse, réseau coupé, serveur indisponible). Plutôt que de laisser Python afficher un long *traceback* technique, on **capture** l'erreur et on affiche un message clair.

```python
try:
    df = pd.read_csv(URL, header=None, na_values="?")
    print(f"Dataset downloaded successfully from {URL}")
except Exception as error:
    raise SystemExit(f"Failed to download dataset from {URL}: {error}") from error
```

Décryptage :
- **`try:`** — on tente l'opération risquée.
- **`except Exception as error:`** — si **n'importe quelle** erreur survient, on la récupère dans `error`.
- **`raise SystemExit("message")`** — arrête le programme avec un message lisible et un code de sortie non nul (signale l'échec au système). C'est la convention adoptée dans tout le projet.
- **`from error`** — conserve l'erreur d'origine dans la « chaîne » d'exceptions (utile pour déboguer).

> `SystemExit` est préférable à un simple `print` + `return` : il **stoppe vraiment** le script et signale l'échec (code retour ≠ 0), ce qu'un outil d'automatisation peut détecter.

---

## Sauvegarder : `df.to_csv(path, index=False)`

Comme dans les autres scripts d'import, `index=False` évite d'écrire la colonne d'index Pandas (0, 1, 2…) dans le fichier de sortie.

```python
df.to_csv(OUTPUT_PATH, index=False)
```

Noter que `to_csv` accepte directement un objet `Path` — pas besoin de le convertir en chaîne.

---

## À retenir

- `pathlib.Path` + l'opérateur `/` construisent des chemins portables ; `.parent` donne le dossier, `.mkdir(parents=True, exist_ok=True)` le crée sans erreur s'il existe.
- `pd.read_csv(URL)` télécharge **et** parse ; `na_values="?"` marque les manquants **dès la lecture**.
- `try/except` + `raise SystemExit("message clair") from error` = arrêt propre et lisible en cas d'échec (convention du projet).
- `to_csv(..., index=False)` pour ne pas polluer le fichier avec l'index Pandas.
