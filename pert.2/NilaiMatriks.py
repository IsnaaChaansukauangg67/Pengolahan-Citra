import cv2

#Membaca gambar dalam Grayscale
img = cv2.imread('C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg', 0)
 
#Mengambil 5x5 pixel pertama
matriks = img[0:5,0:5]

#Menampilkan hasil
print("Matriks 5x5 pertama:")
print(matriks)