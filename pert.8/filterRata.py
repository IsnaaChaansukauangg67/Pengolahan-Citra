import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar grayscale
F = cv2.imread("img1.png", cv2.IMREAD_GRAYSCALE)

# Ukuran gambar
tinggi, lebar = F.shape

# Ubah ke double/float
F2 = F.astype(float)

# Membuat array hasil
G = np.zeros((tinggi, lebar), dtype=np.uint8)

# Proses filter pemerataan (mean filter 3x3)
for baris in range(1, tinggi - 1):
    for kolom in range(1, lebar - 1):

        jum = (
            F2[baris-1, kolom-1] +
            F2[baris-1, kolom] +
            F2[baris-1, kolom+1] +
            F2[baris, kolom-1] +
            F2[baris, kolom] +
            F2[baris, kolom+1] +
            F2[baris+1, kolom-1] +
            F2[baris+1, kolom] +
            F2[baris+1, kolom+1]
        )

        G[baris, kolom] = np.uint8((1/9) * jum)

# Menampilkan hasil
plt.figure(figsize=(10,5))

# Gambar asli
plt.subplot(1,2,1)
plt.imshow(F, cmap='gray')
plt.title("Gambar Asli")
plt.axis("off")

# Hasil filter pemerataan
plt.subplot(1,2,2)
plt.imshow(G, cmap='gray')
plt.title("Hasil Filter Pemerataan")
plt.axis("off")

plt.show()