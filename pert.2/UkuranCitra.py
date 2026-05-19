import cv2

#Membaca gambar
img = cv2.imread('C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg')

#Mengambil ukuran gambar
tinggi, lebar, _ =img.shape

#Menampilkan ukuran
print("Tinggi:", tinggi)
print("Lebar:", lebar)