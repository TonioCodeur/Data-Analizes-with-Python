# Notes d'apprentissage — `test_perf_numpy.py`

> Un script qui **mesure et compare** le temps d'exécution de `iteration.py` (boucles) et `iteration_clean.py` (vectorisé), en neutralisant l'affichage graphique. Il illustre le *chronométrage* et l'exécution d'un script depuis un autre.

## À quoi sert ce script

Les deux scripts d'image ouvrent une fenêtre matplotlib **bloquante** : impossible de les chronométrer tels quels. Ce script :
1. crée de **faux modules** (`matplotlib`, `sklearn`) qui ne font rien, pour éviter l'ouverture de fenêtre et le chargement de la vraie image ;
2. lance chaque script dans un **sous-processus** en pointant vers ces faux modules ;
3. **chronomètre** les deux avec `timeit` et affiche la différence.

C'est un script utilitaire (« harness » de test), plus avancé que les autres — il touche à la bibliothèque standard Python autant qu'à NumPy.

---

## Les modules standard utilisés

| Module | Rôle ici |
|---|---|
| `pathlib.Path` | manipuler les chemins de fichiers proprement |
| `tempfile` | créer un dossier temporaire jetable |
| `textwrap.dedent` | écrire du code sur plusieurs lignes sans souci d'indentation |
| `subprocess` | lancer un autre script Python comme processus séparé |
| `os` / `sys` | variables d'environnement et chemin de l'interpréteur |
| `timeit` | mesurer un temps d'exécution |

---

## Les « stubs » (faux modules)

Un **stub** est une fausse version d'un module qui expose les mêmes noms mais ne fait rien. Ici on remplace :
- `matplotlib.pyplot.imshow` / `show` → des fonctions vides (pas de fenêtre) ;
- `sklearn.datasets.load_sample_image` → renvoie une mini-image `4×4×3` de zéros (pas de vraie image à charger).

```python
# extrait du faux pyplot
def imshow(*args, **kwargs):
    pass
def show():
    pass
```

### `textwrap.dedent`
Permet d'écrire un bloc de code indenté dans le script, puis d'en retirer l'indentation commune avant de l'écrire dans un fichier.

```python
import textwrap
code = textwrap.dedent("""
    def f():
        return 1
""").strip()
# -> "def f():\n    return 1"  (sans les espaces de gauche superflus)
```

### `Path.write_text(...)` / `Path.mkdir(...)`
Écrit un fichier / crée un dossier. `parents=True` crée les dossiers intermédiaires, `exist_ok=True` évite l'erreur si le dossier existe déjà.

---

## Lancer un script dans un sous-processus

### `subprocess.run([...], ...)`
Exécute une commande externe. Ici : `python <script>`.

```python
import subprocess, sys
subprocess.run(
    [sys.executable, "mon_script.py"],   # sys.executable = le python courant
    check=True,          # lève une erreur si le script échoue
    capture_output=True, # récupère la sortie au lieu de l'afficher
    text=True,           # sortie en texte (str) plutôt qu'en octets
)
```

Paramètres clés :
- `sys.executable` = chemin de l'interpréteur Python actif (garantit d'utiliser le bon).
- `env` = variables d'environnement passées au sous-processus.
- `PYTHONPATH` = liste des dossiers où Python cherche les modules → on y met le dossier des stubs **en premier** pour qu'ils masquent les vrais.
- `MPLBACKEND=Agg` = force matplotlib en mode « sans écran » (sécurité supplémentaire).

---

## Chronométrer avec `timeit`

### `timeit.repeat(fonction, repeat=n, number=m)`
Exécute `fonction` `m` fois, répète la mesure `n` fois, et renvoie la **liste** des `n` durées.

```python
import timeit
temps = timeit.repeat(lambda: sum(range(1000)), repeat=3, number=100)
# ex. [0.0021, 0.0019, 0.0020]
```

On prend ensuite le **minimum** (`min(...)`) car c'est la mesure la moins polluée par le système d'exploitation (la plus représentative du « meilleur cas »).

```python
old_time = min(timeit.repeat(lambda: _run_script(SCRIPT_OLD, stub_dir), repeat=2, number=1))
```

> Différence `timeit.timeit` vs `timeit.repeat` :
> - `timeit()` renvoie **un** temps total (cf. `perf.md`).
> - `repeat()` renvoie **plusieurs** temps → on garde le meilleur.

---

## Note sur le nom `test_...`

Le fichier s'appelle `test_perf_numpy.py` et la fonction `test_compare_iteration_scripts`, mais **ce n'est pas un test automatisé** au sens `pytest` : il ne fait pas d'`assert`, il **affiche** les temps. C'est un script de mesure exécuté à la main avec `python test_perf_numpy.py`.

---

## À retenir

- Pour chronométrer un script qui ouvre une fenêtre, on **neutralise** l'affichage avec des **stubs** injectés via `PYTHONPATH`.
- `subprocess.run([sys.executable, script])` lance un script Python comme processus indépendant.
- `timeit.repeat(...)` renvoie plusieurs mesures ; on garde le **minimum** comme référence.
- Ce fichier confirme, chiffres à l'appui, la leçon de `iteration.py` vs `iteration_clean.py` : la vectorisation est plus rapide.
