# EN: Import NumPy, the numerical computing library, aliased as "np".
# FR: Importe NumPy, la bibliothèque de calcul numérique, renommée "np".
import numpy as np

# EN: Create a 2x3 matrix filled with zeros.
# FR: Crée une matrice 2x3 remplie de zéros.
zeros = np.zeros((2, 3))
# EN: Create a 2x3 matrix filled with ones.
# FR: Crée une matrice 2x3 remplie de uns.
ones = np.ones((2, 3))

# EN: axis=0 stacks the matrices vertically (one on top of the other) -> shape (4, 3).
# FR: axis=0 empile les matrices verticalement (l'une sur l'autre) -> forme (4, 3).
matrix_concatenated_y = np.concatenate((zeros, ones), axis=0)
print(matrix_concatenated_y)

# EN: axis=1 joins the matrices horizontally (side by side) -> shape (2, 6).
# FR: axis=1 accole les matrices horizontalement (côte à côte) -> forme (2, 6).
matrix_concatenated_x = np.concatenate((zeros, ones), axis=1)
print(matrix_concatenated_x)
