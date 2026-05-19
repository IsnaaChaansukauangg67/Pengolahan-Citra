import cv2
import matplotlib.pyplot as plt

#Membaca gmb berwarna
img = cv2.imread('C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg')

#Konversi ke grayscale
gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Biner (threshold 128)
biner = (gray < 128).astype('uint8')

#Negatif
negatif = 255 - gray

#Subplot
plt.figure(figsize=(8,6))

#Citra asli (conv. BGR to RGB biar warna normal)
plt.subplot(2,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Citra Asli')
plt.axis('off')

#Grayscale
plt.subplot(2,2,2)
plt.imshow(gray, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

#Biner
plt.subplot(2,2,3)
plt.imshow(biner, cmap='gray')
plt.title('Biner')
plt.axis('off')

#Negatif
plt.subplot(2,2,4)
plt.imshow(negatif, cmap='gray')
plt.title('Negatif')
plt.axis('off')

plt.tight_layout()
plt.show()