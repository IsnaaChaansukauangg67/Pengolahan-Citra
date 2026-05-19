import cv2

#Membaca gambar dalam Grayscale
img = cv2.imread('C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg')

#Menampilkan nilai pixel di koordinat (x=10, y=20)
x = 10
y = 20

nilai_pixel = img[y, x]

print(f"Nilai pixel di ({x},{y}):", nilai_pixel)
