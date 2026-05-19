import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("img1.png")

# Ubah ke RGB agar warna benar saat ditampilkan
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Filter noise menggunakan Gaussian Blur
hasil = cv2.GaussianBlur(img_rgb, 5)

# Menampilkan hasil
plt.figure(figsize=(12,6))

# Gambar asli
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Gambar Asli")
plt.axis("off")

# Gambar setelah noise reduction
plt.subplot(1,2,2)
plt.imshow(hasil)
plt.title("Hasil Filter Median")
plt.axis("off")

plt.show()

