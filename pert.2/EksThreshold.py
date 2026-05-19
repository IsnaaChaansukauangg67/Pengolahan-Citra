import cv2
import matplotlib.pyplot as plt

#Membaca gmb grayscale
img = cv2.imread('C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg', 0)

threshold = [50, 100, 150, 200]

plt.figure(figsize=(10, 6))

#Tampilkan gmb asli
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Asli (Grayscale)')
plt.axis('off')

#Loop threshold
for i, t in enumerate(threshold) :
    biner = (img < t).astype('uint8')
    
    plt.subplot(2, 3, i+2)
    plt.imshow(img, cmap='gray')
    plt.title(f'Thershold {t}')
    plt.axis('off')
    
plt.tight_layout()
plt.show()