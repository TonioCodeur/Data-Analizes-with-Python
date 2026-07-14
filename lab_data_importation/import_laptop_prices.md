# Notes d'apprentissage — `import_laptop_prices.py`

> Même patron de **pipeline d'import/nettoyage** que `import_auto.py`, appliqué au jeu de données « prix des ordinateurs portables » (lab IBM). Ici le nettoyage est plus léger : on nomme les colonnes et on marque les `?` en `NaN`, **sans** supprimer de lignes.

## À quoi sert ce script

1. **télécharger** le CSV `laptop_pricing_dataset_base.csv` (IBM Skills Network) ;
2. le **charger** sans en-tête ;
3. le **nettoyer** : nommer les 12 colonnes, remplacer `?` par `NaN` ;
4. le **sauvegarder** ;
5. l'**afficher** (aperçu, types, stats, info).

Reportez-vous à `import_auto.md` pour le détail de chaque fonction — cette note se concentre sur **ce qui diffère**.

---

## Les 12 colonnes du jeu de données

```python
COLUMN_HEADERS = [
    "Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core",
    "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD",
    "Weight_kg", "Price",
]
```

Ces noms remplacent la numérotation 0–11 attribuée par `pd.read_csv(..., header=None)`.

---

## La différence clé : un nettoyage sans suppression

```python
def clean_dataset(df):
    df.columns = COLUMN_HEADERS
    return df.replace("?", np.nan)      # on marque les manquants, on ne supprime PAS
```

Contrairement à `import_auto.py` qui faisait `dropna(subset=["price"])`, ce script **conserve toutes les lignes**. Il se contente de convertir les marqueurs `?` en `NaN`.

Pourquoi ce choix ? Deux stratégies opposées de gestion des valeurs manquantes :

| Stratégie | Méthode | Quand l'utiliser |
|---|---|---|
| **Supprimer** | `df.dropna(...)` | quand la donnée manquante rend la ligne inutilisable |
| **Signaler / garder** | `df.replace("?", np.nan)` seul | quand on veut décider plus tard (imputation, analyse par colonne) |
| **Remplir (imputer)** | `df.fillna(valeur)` | remplacer par la moyenne, la médiane, le mode… |

Exemple d'imputation qu'on ferait à l'étape suivante d'une vraie analyse :
```python
# remplacer les prix manquants par le prix moyen
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Price"] = df["Price"].fillna(df["Price"].mean())
```

> `pd.to_numeric(..., errors="coerce")` convertit une colonne texte en nombres et transforme en `NaN` tout ce qui n'est pas convertible — indispensable après un `read_csv` où une colonne numérique contenait des `?` et est donc restée en type `object` (texte).

---

## Pourquoi les colonnes numériques peuvent rester en texte

Quand une colonne contient ne serait-ce qu'un `?`, Pandas la lit comme du **texte** (`object`). Même après `replace("?", np.nan)`, son `dtype` peut rester `object`. C'est visible dans la sortie de `summarize_dataset` :

```python
print(df.dtypes)   # ex. RAM_GB -> object au lieu de int64
```

D'où l'intérêt de `pd.to_numeric(..., errors="coerce")` pour « re-typer » proprement ces colonnes avant tout calcul (moyenne, corrélation…).

---

## Le résumé : `df.head(10)` et compagnie

Identique à `import_auto.py`, avec un aperçu de **10** lignes :

```python
print(df.head(10))                 # 10 premières lignes
print(df.dtypes)                   # types (repère les object suspects)
print(df.describe(include="all"))  # stats complètes
df.info()                          # valeurs non nulles par colonne
```

Voir `../Pandas/dataframe.md` pour le détail de ces méthodes d'inspection.

---

## À retenir

- Ce script réutilise le **même pipeline** que `import_auto.py` (download → read → clean → save → summarize).
- Sa spécificité : nettoyage **minimal** (`replace("?", np.nan)`) qui **conserve** toutes les lignes.
- Trois stratégies pour les valeurs manquantes : **supprimer** (`dropna`), **signaler** (`replace → NaN`), **imputer** (`fillna`).
- Une colonne contenant des `?` est lue en `object` ; `pd.to_numeric(..., errors="coerce")` la reconvertit en nombres.
