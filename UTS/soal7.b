import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("dokumen.jpeg")

# Resize agar lebih ringan
ratio = img.shape[0] / 500.0
orig = img.copy()

img_resize = cv2.resize(img, (500,
               int(img.shape[0] / ratio)))

# Grayscale
gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Edge Detection
edged = cv2.Canny(blur, 75, 200)

# Cari kontur
contours, _ = cv2.findContours(edged.copy(),
                               cv2.RETR_LIST,
                               cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours,
                  key=cv2.contourArea,
                  reverse=True)[:5]

# Cari bentuk 4 sisi
for c in contours:
    peri = cv2.arcLength(c, True)

    approx = cv2.approxPolyDP(c,
                              0.02 * peri,
                              True)

    if len(approx) == 4:
        screenCnt = approx
        break

# Gambar sudut dokumen
cv2.drawContours(img_resize,
                 [screenCnt],
                 -1,
                 (0,255,0), 2)

# Crop area dokumen
x, y, w, h = cv2.boundingRect(screenCnt)

cropped = img_resize[y:y+h, x:x+w]

# Tampilkan hasil
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img_resize,
                        cv2.COLOR_BGR2RGB))
plt.title("Deteksi Dokumen")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(cropped,
                        cv2.COLOR_BGR2RGB))
plt.title("Hasil Cropping")
plt.axis("off")

plt.show()

