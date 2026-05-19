import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("img1.png")

# Ubah ke RGB agar warna tampil benar di matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur untuk mengurangi noise
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Filter batas / edge detection
edges = cv2.Canny(blur, 100, 200)

# Menampilkan efek filter
plt.figure(figsize=(12,6))

# Gambar asli
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Gambar Asli")
plt.axis("off")

# Hasil filter batas
plt.subplot(1,2,2)
plt.imshow(edges, cmap='gray')
plt.title("Efek Filter Batas")
plt.axis("off")

plt.show()