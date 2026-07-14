# EN: matplotlib.pyplot is used to display images/plots.
# FR: matplotlib.pyplot sert à afficher des images/graphiques.
import matplotlib.pyplot as plt
# EN: scikit-learn ships a few sample images; we load one of them.
# FR: scikit-learn fournit quelques images d'exemple ; on en charge une.
from sklearn.datasets import load_sample_image

# EN: NumPy for array manipulation of the image pixels.
# FR: NumPy pour manipuler les pixels de l'image sous forme de tableau.
import numpy as np

# EN: Load the sample "flower.jpg" as a NumPy array of shape (height, width, 3=RGB).
# FR: Charge l'image d'exemple "flower.jpg" en tableau NumPy de forme (hauteur, largeur, 3=RVB).
flower = load_sample_image('flower.jpg')

# EN: This block converts the image to grayscale with explicit nested loops (slow way).
# FR: Ce bloc convertit l'image en niveaux de gris avec des boucles imbriquées (méthode lente).
output = []
for line in flower:            # EN: iterate over each row / FR: parcourt chaque ligne
  for pixel in line:           # EN: iterate over each pixel / FR: parcourt chaque pixel
    # EN: average of the 3 RGB channels = the gray level of the pixel.
    # FR: moyenne des 3 canaux RVB = le niveau de gris du pixel.
    moyenne = int(np.mean(pixel))
    # EN: repeat the gray value on 3 channels so it stays a valid RGB pixel.
    # FR: répète la valeur de gris sur 3 canaux pour rester un pixel RVB valide.
    moyenne_3d = np.stack((moyenne, moyenne, moyenne))
    output.append(moyenne_3d)
# EN: rebuild the flat list of pixels into the original image shape.
# FR: reconstruit la liste plate de pixels dans la forme d'origine de l'image.
img_black_and_white = np.array(output).reshape(flower.shape)
# EN: stack the grayscale image above the original (axis=0) and display them.
# FR: empile l'image en gris au-dessus de l'originale (axis=0) et les affiche.
plt.imshow(np.concatenate((img_black_and_white, flower), axis=0))
plt.show()
