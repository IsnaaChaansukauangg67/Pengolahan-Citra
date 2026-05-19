import cv2

#Membaca gambar berwarna
img = cv2.imread('C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg')

#Mengambil channel B, G, R
B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

#KOnversi ke grayscale manual
gray = 0.2989 * R + 0.5870 * G + 0.1141 * B

#Ubah ke tipe uint8
gray = gray.astype('uint8')

#Menampilkan hasil
cv2.imshow('Grayscale Manual', gray)
cv2.waitKey(0)
cv2.destroyAllWindos()