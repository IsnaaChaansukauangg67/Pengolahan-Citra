import cv2
import matplotlib.pyplot as plt

# Membaca gambar grayscale
img = cv2.imread("img1.png", cv2.IMREAD_GRAYSCALE)

# Menghilangkan noise menggunakan Median Filter
# Cocok untuk noise bintik putih seperti pada gambar mobil
hasil = cv2.medianBlur(img, 5)

# Menampilkan hasil
plt.figure(figsize=(10,5))

# Gambar asli
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Gambar Asli")
plt.axis("off")

# Hasil setelah noise dihilangkan
plt.subplot(1,2,2)
plt.imshow(hasil, cmap='gray')
plt.title("Hasil Filter Batas")
plt.axis("off")

plt.show()
