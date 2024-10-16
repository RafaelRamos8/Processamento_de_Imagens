import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lê a imagem em escala de cinza
imagem = cv2.imread('coffe.jpeg', cv2.IMREAD_GRAYSCALE)

# Aplicando o filtro de mediana com diferentes tamanhos de kernel
mediana_3 = cv2.medianBlur(imagem, 3)  # Kernel 3x3
mediana_21 = cv2.medianBlur(imagem, 21)  # Kernel 20x20
mediana_51 = cv2.medianBlur(imagem, 51)  # Kernel 50x50

# Mostrar as imagens com matplotlib
plt.figure(figsize=(15, 10))

# Imagem original
plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title("Imagem Original")
plt.axis("off")

# Filtro de mediana 5x5
plt.subplot(2, 2, 2)
plt.imshow(mediana_3, cmap='gray')
plt.title("Filtro de Mediana 3x3")
plt.axis("off")

# Filtro de mediana 11x11
plt.subplot(2, 2, 3)
plt.imshow(mediana_21, cmap='gray')
plt.title("Filtro de Mediana 21x21")
plt.axis("off")

# Filtro de mediana 21x21
plt.subplot(2, 2, 4)
plt.imshow(mediana_51, cmap='gray')
plt.title("Filtro de Mediana 51x51")
plt.axis("off")

plt.show()
