# Data analyse — Apprentissage / Learning

> **FR :** Ce dépôt rassemble mon travail d'**apprentissage de l'analyse de données avec Python**, réalisé dans le cadre d'une **formation certifiée par IBM** (le géant de l'informatique). Ce n'est pas une application : c'est un bac à sable pédagogique où chaque dossier explore une notion à travers de petits scripts autonomes.
>
> **EN:** This repository gathers my work **learning data analysis with Python**, done as part of an **IBM-certified training program** (the computing giant). It is not an application: it is a learning sandbox where each folder explores one concept through small standalone scripts.

---

## Contexte / Context

**FR :** Je suis actuellement une formation en data science avec Python, certifiée par IBM, qui couvre :
- l'**analyse de données** avec les bibliothèques **Pandas** et **NumPy** ;
- le **RAG** et l'**IA agentique** ;
- le **machine learning**.

Ce dépôt contient les scripts, les labs et les notes issus de ce parcours. Les jeux de données proviennent notamment de l'**IBM Skills Network**.

**EN:** I am currently following an IBM-certified data science training with Python, covering:
- **data analysis** with the **Pandas** and **NumPy** libraries;
- **RAG** and **agentic AI**;
- **machine learning**.

This repository holds the scripts, labs and notes from that journey. The datasets come in particular from the **IBM Skills Network**.

---

## Sommaire des dossiers / Folder overview

| Dossier / Folder | Contenu / Content |
|---|---|
| [`NumPy/`](NumPy/) | Fondamentaux de NumPy et traitement d'images (boucles vs vectorisation) / NumPy fundamentals and image processing (loops vs vectorization) |
| [`Pandas/`](Pandas/) | Indexation et sélection dans un DataFrame / DataFrame indexing and selection |
| [`lab_data_importation/`](lab_data_importation/) | Lab IBM : télécharger et nettoyer des jeux de données CSV / IBM lab: download and clean CSV datasets |
| [`premieres_analyses_avec_pandas/`](premieres_analyses_avec_pandas/) | Premières expériences d'import avec pandas / First pandas import experiments |
| `perf.py` | Comparaison de performance : boucle Python pure vs `np.sum` / Performance comparison: pure Python loop vs `np.sum` |

**FR :** Chaque dossier possède son propre `README.md` détaillé — commencez par celui du dossier qui vous intéresse.
**EN:** Each folder has its own detailed `README.md` — start with the one for the folder you're interested in.

---

## Installation / Setup

**FR :** Windows + PowerShell, Python 3.14. Toutes les dépendances du projet sont regroupées dans [`requirements.txt`](requirements.txt) (numpy, pandas, matplotlib, scikit-learn).
**EN:** Windows + PowerShell, Python 3.14. All project dependencies are listed in [`requirements.txt`](requirements.txt) (numpy, pandas, matplotlib, scikit-learn).

```powershell
# À la racine du projet / from the repo root
python -m venv .venv                       # si besoin / if needed (un .venv existe déjà)
.\.venv\Scripts\Activate.ps1               # activer / activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**FR :** Sous macOS / Linux, remplacez la ligne d'activation par `source .venv/bin/activate`.
**EN:** On macOS / Linux, replace the activation line with `source .venv/bin/activate`.

---

## Exécuter les scripts / Running the scripts

```powershell
python perf.py
python NumPy\discover.py
python Pandas\dataframe.py
python lab_data_importation\import_auto.py   # interactif : demande un nom de fichier / interactive: prompts for a file name
```

> **FR :** Les scripts `NumPy\iteration*.py` ouvrent une **fenêtre image bloquante** (matplotlib) — fermez-la pour terminer.
> **EN:** The `NumPy\iteration*.py` scripts open a **blocking image window** (matplotlib) — close it to finish.

---

## Conventions

- **FR :** La prose (commentaires, sorties `print`, README) est en **français** ; le code (identifiants, docstrings) est en **anglais**.
- **EN:** Prose (comments, `print` output, READMEs) is in **French**; code (identifiers, docstrings) is in **English**.

---

## À propos de la certification / About the certification

**FR :** Cette formation est certifiée par **IBM**, acteur historique et majeur du secteur informatique et de la data science. Les compétences visées : manipuler et nettoyer des données, les analyser avec Pandas et NumPy, puis progresser vers le machine learning et l'IA.

**EN:** This training is certified by **IBM**, a historic and major player in the computing and data science industry. The targeted skills: manipulating and cleaning data, analyzing it with Pandas and NumPy, then moving on to machine learning and AI.
