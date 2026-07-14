# EN: Import the NumPy library, aliased as "np" (the community convention).
# FR: Importe la bibliothèque NumPy, renommée "np" (convention de la communauté).
import numpy as np

# EN: Getting started with NumPy — creating a simple 1D array (vector).
# FR: Découverte de NumPy — création d'un simple tableau 1D (vecteur).
arr = np.array([1, 2, 3])

# EN: np.__version__ returns the installed NumPy version.
# FR: np.__version__ renvoie la version de NumPy installée.
print("Version de NumPy :", np.__version__)
# EN: Display the array itself.
# FR: Affiche le tableau lui-même.
print("Array            :", arr)
# EN: .dtype gives the data type of the elements (e.g. int64).
# FR: .dtype donne le type de données des éléments (ex. int64).
print("Type             :", arr.dtype)
# EN: .ndim gives the number of dimensions (1 for a vector, 2 for a matrix...).
# FR: .ndim donne le nombre de dimensions (1 pour un vecteur, 2 pour une matrice...).
print("Dimensions       :", arr.ndim)
# EN: .shape gives the shape as a tuple, here (3,) = 3 elements.
# FR: .shape donne la forme sous forme de tuple, ici (3,) = 3 éléments.
print("Forme (shape)    :", arr.shape)
# EN: .sum() returns the sum of all elements.
# FR: .sum() renvoie la somme de tous les éléments.
print("Somme            :", arr.sum())
# EN: .mean() returns the arithmetic mean of the elements.
# FR: .mean() renvoie la moyenne arithmétique des éléments.
print("Moyenne          :", arr.mean())
# EN: Multiplying by a scalar applies the operation to every element (vectorization).
# FR: La multiplication par un scalaire s'applique à chaque élément (vectorisation).
print("Array * 2        :", arr * 2)

# EN: np.ones creates a matrix of shape (4, 3) filled with 1.0.
# FR: np.ones crée une matrice de forme (4, 3) remplie de 1.0.
arr2 = np.ones((4, 3))
print("Array 2          :")
print(arr2)

# EN: np.zeros creates a matrix of shape (9, 7) filled with 0.0.
# FR: np.zeros crée une matrice de forme (9, 7) remplie de 0.0.
arr3 = np.zeros((9, 7))
print("Array 3          :")
print(arr3)
# EN: arr3[:, 5] selects all rows of column index 5 (the 6th column).
# FR: arr3[:, 5] sélectionne toutes les lignes de la colonne d'index 5 (la 6ème colonne).
print(arr3[:, 5])  # Affiche la 6ème colonne de arr3

# EN: Build an array of 300 values from 0.00 to 2.99 using a list comprehension.
# FR: Construit un tableau de 300 valeurs de 0.00 à 2.99 via une compréhension de liste.
x = np.array([_/100 for _ in range(300)])
print("Array x          :")
print(x)
# EN: NumPy "universal functions" (ufuncs) apply element-wise to the whole array.
# FR: Les "fonctions universelles" (ufuncs) de NumPy s'appliquent élément par élément.
print(np.exp(x))  # Affiche l'exponentielle de chaque élément de x
print(np.cos(x))  # Affiche le cosinus de chaque élément de x
print(np.sin(x))  # Affiche le sinus de chaque élément de x
print(np.log(x))  # Affiche le logarithme de chaque élément de x
# EN: np.round rounds each value; decimals=2 keeps 2 digits after the point.
# FR: np.round arrondit chaque valeur ; decimals=2 conserve 2 chiffres après la virgule.
print(np.round(np.exp(x), decimals=2))  # Affiche l'exponentielle arrondie à 2 décimales
