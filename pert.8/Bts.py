import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("img1.png")

# Ubah ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Mengurangi noise terlebih dahulu
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Filter batas / Edge Detection (Canny)
edges = cv2.Canny(blur, 100, 200)

# Menampilkan hasil
plt.figure(figsize=(12,6))

# Gambar asli
plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Gambar Asli")
plt.axis("off")

# Hasil filter batas
plt.subplot(1,2,2)
plt.imshow(edges, cmap='gray')
plt.title("Hasil Filter Batas")
plt.axis("off")

plt.show()