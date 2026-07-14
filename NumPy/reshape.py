# EN: Standard-library random module (imported here but not actually used below).
# FR: Module random de la bibliothèque standard (importé ici mais non utilisé ci-dessous).
import random as rd

# EN: Import NumPy for array creation and reshaping.
# FR: Importe NumPy pour la création et le redimensionnement de tableaux.
import numpy as np

# EN: Build a 1D array of the integers 1..9 with a list comprehension.
# FR: Construit un tableau 1D des entiers 1..9 via une compréhension de liste.
matrix = np.array([i for i in range(1, 10)])
print(matrix)

# EN: .reshape((3, 3)) reorganizes the 9 values into a 3x3 matrix (same data).
# FR: .reshape((3, 3)) réorganise les 9 valeurs en une matrice 3x3 (mêmes données).
matrix_reshaped = matrix.reshape((3, 3))
print(matrix_reshaped)
# EN: Reshape back to a single row (1, 9). The element count must stay the same.
# FR: Redimensionne en une seule ligne (1, 9). Le nombre d'éléments doit rester identique.
print(matrix_reshaped.reshape((1, 9)))

# EN: A 5x4 matrix (20 elements) filled with zeros.
# FR: Une matrice 5x4 (20 éléments) remplie de zéros.
matrix_zero = np.zeros((5, 4))
print(matrix_zero)

# EN: 20 elements can be reshaped to (2, 10) because 2*10 == 5*4 == 20.
# FR: 20 éléments peuvent être redimensionnés en (2, 10) car 2*10 == 5*4 == 20.
matrix_zero_reshaped = matrix_zero.reshape((2, 10))
print(matrix_zero_reshaped)

# EN: A 10x10 matrix of random integers between 0 and 99.
# FR: Une matrice 10x10 d'entiers aléatoires entre 0 et 99.
matrix_random = np.random.randint(0, 100, size=(10, 10))
print(matrix_random)
# EN: Boolean masking: every element <= 17 is set to 0 in one vectorized step.
# FR: Masque booléen : chaque élément <= 17 est mis à 0 en une seule étape vectorisée.
matrix_random[matrix_random <= 17] = 0
print(matrix_random)
