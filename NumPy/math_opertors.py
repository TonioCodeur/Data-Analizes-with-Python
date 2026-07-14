# EN: Import NumPy for numerical arrays and operations.
# FR: Importe NumPy pour les tableaux et opérations numériques.
import numpy as np

# EN: Two 1D arrays (vectors) of 3 elements each.
# FR: Deux tableaux 1D (vecteurs) de 3 éléments chacun.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# EN: Fix the random seed so the "random" numbers are reproducible.
# FR: Fixe la graine aléatoire pour que les nombres "aléatoires" soient reproductibles.
np.random.seed(30)
# EN: Two 3x3 matrices of random integers in [0, 10[.
# FR: Deux matrices 3x3 d'entiers aléatoires dans [0, 10[.
matrix = np.random.randint(0, 10, size=(3, 3))
matrix2 = np.random.randint(0, 10, size=(3, 3))

# EN: Scalar multiplication: each element of arr1 is multiplied by 2.
# FR: Multiplication par un scalaire : chaque élément de arr1 est multiplié par 2.
print(2 * arr1)
# EN: Element-wise multiplication (Hadamard product), NOT a matrix product.
# FR: Multiplication élément par élément (produit de Hadamard), PAS un produit matriciel.
print(arr1 * arr2)
# EN: Element-wise addition.
# FR: Addition élément par élément.
print(arr1 + arr2)
# EN: The @ operator on two vectors gives the dot product (a single number).
# FR: L'opérateur @ sur deux vecteurs donne le produit scalaire (un seul nombre).
print(arr1 @ arr2)  # Produit scalaire des deux vecteurs / dot product of the two vectors
# EN: The @ operator on two 2D matrices performs true matrix multiplication.
# FR: L'opérateur @ sur deux matrices 2D effectue une vraie multiplication matricielle.
print(matrix @ matrix2)  # This will perform matrix multiplication

# EN: Join the two matrices horizontally (axis=1) into a 3x6 matrix.
# FR: Accole les deux matrices horizontalement (axis=1) en une matrice 3x6.
fusion_matrix = np.concatenate((matrix, matrix2), axis=1)
print(fusion_matrix)

# EN: np.sum adds up every element of the whole matrix.
# FR: np.sum additionne tous les éléments de la matrice entière.
print(np.sum(fusion_matrix))  # This will compute the sum of all elements in the matrix
# EN: .prod() multiplies every element together.
# FR: .prod() multiplie tous les éléments entre eux.
print(fusion_matrix.prod())  # This will compute the product of all elements in the matrix
