import cv2

# Baca gambar grayscale
img = cv2.imread('C:/Users/isna/Documents/Pengolahan Citra/praktik/img.2.jpeg', 0)

#Resize (opsional)
kecil = cv2.resize(img, (200, 200))
# Threshold
threshold = 128
biner = (img < threshold).astype('uint8')

# Tampilkan dua gambar
cv2.imshow('Grayscale', img)
cv2.imshow('Citra Biner', biner * 255)

cv2.waitKey(0)
cv2.destroyAllWindows()