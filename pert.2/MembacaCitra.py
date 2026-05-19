import cv2

#Membaca gambar
img = cv2.imread('C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg')

#Menampilkan Citra
cv2.imshow('Citra', img)
cv2.waitKey(0)
cv2.destroyAllWindows()