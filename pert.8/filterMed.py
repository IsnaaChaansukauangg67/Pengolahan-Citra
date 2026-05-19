import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar grayscale
F = cv2.imread("img1.png", cv2.IMREAD_GRAYSCALE)

# Ukuran gambar
tinggi, lebar = F.shape

# Membuat array hasil
G = np.zeros((tinggi, lebar), dtype=np.uint8)

# Proses filter median
for baris in range(1, tinggi - 1):
    for kolom in range(1, lebar - 1):

        # Ambil data piksel tetangga 3x3
        data = [
            F[baris-1, kolom-1],
            F[baris-1, kolom],
            F[baris-1, kolom+1],
            F[baris,   kolom-1],
            F[baris,   kolom],
            F[baris,   kolom+1],
            F[baris+1, kolom-1],
            F[baris+1, kolom],
            F[baris+1, kolom+1]
        ]

        # Urutkan data
        data.sort()

        # Ambil nilai median (elemen ke-5)
        G[baris, kolom] = data[4]

# Menampilkan hasil
plt.figure(figsize=(10,5))

# Gambar asli
plt.subplot(1,2,1)
plt.imshow(F, cmap='gray')
plt.title("Gambar Asli")
plt.axis("off")

# Hasil filter median
plt.subplot(1,2,2)
plt.imshow(G, cmap='gray')
plt.title("Hasil Filter Median")
plt.axis("off")

plt.show()