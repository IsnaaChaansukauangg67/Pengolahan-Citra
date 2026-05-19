import cv2

#Membaca gmr grayscale
img = cv2.imread('C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg', 0)

#Membuat citra negatif
negatif = 255 - img

#Menampilkan hasil
cv2.imshow('Grayscale', img)
cv2.imshow('Citra Negatif', negatif)

#Menyimpan hasil ke file baru
cv2.imwrite('negatif_C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg', negatif)

cv2.waitKey(0)
cv2.destroyAllWindowa()