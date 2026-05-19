import cv2
import numpy as np

#Membaca gmb grayscale
img = cv2.imread('C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg', 0)

#Kuantisasi 4 bit (16 level)
q4 = (img // 16) * 16

#Kuantisasi 2 bit (4 level)
q2 = (img // 64) * 64

#Menampilkan hasil
cv2.imshow('Greeyscale Asli', img)
cv2.imshow('4 bit (16 level)', q4)
cv2.imshow('2 bit (4 level)', q2)

cv2.waitKey(0)
cv2.destroyAllWindows()