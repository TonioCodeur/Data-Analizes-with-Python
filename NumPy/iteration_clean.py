# EN: matplotlib.pyplot to display the resulting image.
# FR: matplotlib.pyplot pour afficher l'image résultante.
import matplotlib.pyplot as plt
# EN: scikit-learn sample images loader.
# FR: chargeur d'images d'exemple de scikit-learn.
from sklearn.datasets import load_sample_image

# EN: NumPy for the vectorized image processing.
# FR: NumPy pour le traitement d'image vectorisé.
import numpy as np

# EN: Load "flower.jpg" as a (height, width, 3) RGB array.
# FR: Charge "flower.jpg" en tableau RVB (hauteur, largeur, 3).
flower = load_sample_image('flower.jpg')

# EN: axis=2 averages the 3 color channels -> a (height, width) grayscale array.
#     This is the fast, vectorized equivalent of the loops in iteration.py.
# FR: axis=2 fait la moyenne des 3 canaux -> un tableau (hauteur, largeur) en gris.
#     C'est l'équivalent rapide et vectorisé des boucles de iteration.py.
moyenne = np.mean(flower, axis=2, dtype=int)
# EN: np.repeat duplicates each gray value 3 times, then reshape restores the RGB shape.
# FR: np.repeat duplique chaque valeur de gris 3 fois, puis reshape restaure la forme RVB.
img_np = np.repeat(moyenne, 3).reshape(flower.shape)
# EN: Show the grayscale image stacked on top of the original.
# FR: Affiche l'image en gris empilée au-dessus de l'originale.
plt.imshow(np.concatenate((img_np, flower), axis=0))
plt.show()
