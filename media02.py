import cv2
import numpy as np
import matplotlib.pyplot as plt

#Lê a imagem em escala de cinza
imagem = cv2.imread('coffe.jpeg', cv2.IMREAD_GRAYSCALE)

#aplicando o filtro de media com tamanho 3x3
filtro_3X3 = cv2.blur(imagem, (3, 3))

#Aplicando o filtro de media com tamanho 5X5
filtro_5x5 = cv2.blur(imagem, (5, 5))

#aplicando filtro de media com tamanho 50x50
filtro_50x50 = cv2.blur(imagem, (50, 50))

#Mostrar as imagens com matplotlib
plt.figure(figsize=(15, 10))

#Imagem original
plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title("Imagem Original")
plt.axis("off")

#filtro 7x7
plt.subplot(2, 2, 2)
plt.imshow(filtro_3X3, cmap='gray')
plt.title("Filtro de media 3x3")
plt.axis("off")

#filtro 15x15
plt.subplot(2, 2, 3)
plt.imshow(filtro_5x5, cmap='gray')
plt.title("Filtro de media 5x5")
plt.axis("off")

#filtro 25x25
plt.subplot(2, 2, 4)
plt.imshow(filtro_50x50, cmap='gray')
plt.title("Filtro de media 50x50")
plt.axis("off")

plt.show()