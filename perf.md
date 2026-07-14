# Notes d'apprentissage — `perf.py`

> Le **benchmark racine** du projet : comparer une somme faite avec une **boucle `for` pure Python** contre `np.sum` (NumPy), grâce au module `timeit`. Démonstration chiffrée du gain de la vectorisation.

## À quoi sert ce script

Il crée un tableau d'un million de nombres aléatoires, puis mesure le temps que met :
- une **boucle Python** (`sum(list)` et une fonction `somme_for`) ;
- **NumPy** (`arr.sum()`).

Il affiche les deux temps et le **facteur d'accélération** (`≈ N× plus rapide`). C'est la version « pure calcul » du contraste illustré en images par `NumPy/iteration*.py`.

---

## Structure du script

Contrairement aux scripts d'exploration NumPy (code au niveau global), `perf.py` adopte la forme **fonctions + garde `__main__`** :

```python
def somme_for(data): ...
def somme_numpy(data): ...
def main(): ...

if __name__ == "__main__":
    main()
```

### La garde `if __name__ == "__main__":`
Ce bloc ne s'exécute **que** si le fichier est lancé directement (`python perf.py`), pas s'il est importé depuis un autre module. C'est la convention Python pour séparer « code exécutable » et « code réutilisable ».

```python
# fichier a.py
def util(): ...
if __name__ == "__main__":
    print("lancé directement")   # ne s'affiche pas si on fait `import a`
```

---

## `timeit` — mesurer un temps d'exécution

### `timeit.timeit(fonction, number=n)`
Exécute `fonction` `n` fois et renvoie le **temps total** (en secondes). On passe la fonction sous forme de `lambda` pour qu'elle ne soit **pas exécutée tout de suite** mais chronométrée par `timeit`.

```python
import timeit
total = timeit.timeit(lambda: sum(range(1000)), number=50)
# temps cumulé des 50 exécutions
temps_moyen = total / 50
```

> **Pourquoi une `lambda` ?** Si on écrivait `timeit.timeit(sum(lst))`, `sum(lst)` serait calculé **avant** l'appel et on chronométrerait « rien ». La `lambda` diffère l'exécution.

Ici le script mesure de deux façons :
1. `number=50` pour un temps cumulé lisible ;
2. `number=n` puis division par `n` (`/ n`) pour obtenir un **temps moyen par exécution**, converti en millisecondes (`* 1000`).

---

## Générer les données

### `np.random.rand(n)`
Crée un tableau de `n` flottants aléatoires dans `[0, 1[`.

```python
np.random.rand(5)     # ex. [0.37 0.95 0.73 0.60 0.16]
```

### `.tolist()`
Convertit le tableau NumPy en **liste Python** classique — nécessaire pour comparer équitablement la boucle Python (`sum(lst)`) et NumPy (`arr.sum()`) sur les mêmes valeurs.

```python
arr = np.array([1, 2, 3])
arr.tolist()          # [1, 2, 3]  (des int Python, plus des int64 NumPy)
```

---

## Les deux approches comparées

### Boucle pure Python
```python
def somme_for(data):
    total = 0.0
    for x in data:
        total += x
    return total
```
Chaque addition repasse par l'interpréteur Python : lent sur un million d'éléments.

### NumPy vectorisé
```python
def somme_numpy(data):
    return data.sum()      # boucle interne en C, sur toute la donnée en bloc
```

Le résultat numérique est **identique** ; seul le temps change radicalement.

---

## Formatage de la sortie (f-strings)

Le script utilise des **f-strings** avec spécificateurs de format :

```python
print(f"np.sum() : {t_numpy * 1000:8.3f} ms")   # 8.3f = largeur 8, 3 décimales
print(f"→ NumPy ~{t_for / t_numpy:.0f}x plus rapide")  # .0f = entier arrondi
```

| Format | Signification |
|---|---|
| `:.3f` | 3 chiffres après la virgule |
| `:8.3f` | largeur minimale 8 caractères, 3 décimales (aligne les colonnes) |
| `:.0f` | arrondi à l'entier |
| `:.6f` | 6 décimales (utile pour des temps très courts) |

---

## À retenir

- `timeit.timeit(lambda: ..., number=n)` chronomètre `n` exécutions ; la **lambda** diffère l'appel.
- On divise par `n` pour un temps **moyen**, on multiplie par 1000 pour des **millisecondes**.
- `np.random.rand(n)` génère des flottants ; `.tolist()` reconvertit en liste Python.
- Résultat identique, mais `np.sum` est **massivement plus rapide** qu'une boucle `for` : la leçon centrale du projet, ici mesurée.
- La garde `if __name__ == "__main__":` sépare le code exécutable du code importable.
