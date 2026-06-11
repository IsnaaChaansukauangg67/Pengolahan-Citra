import cv2
import numpy as np
import matplotlib.pyplot as plt

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

img = cv2.imread('dokumen.jpeg')
orig = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9, 9), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
thresh = cv2.bitwise_not(thresh)

coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle

(h, w) = img.shape[:2]
Mrot = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
rotated = cv2.warpAffine(orig, Mrot, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

gray2 = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(cv2.GaussianBlur(gray2, (5, 5), 0), 75, 200)

contours, _ = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

doc_cnt = None
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        doc_cnt = approx
        break

if doc_cnt is None:
    raise ValueError("Kontur dokumen tidak ditemukan")

pts = order_points(doc_cnt.reshape(4, 2))
(tl, tr, br, bl) = pts

widthA = np.linalg.norm(br - bl)
widthB = np.linalg.norm(tr - tl)
maxWidth = int(max(widthA, widthB))

heightA = np.linalg.norm(tr - br)
heightB = np.linalg.norm(tl - bl)
maxHeight = int(max(heightA, heightB))

dst = np.array([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]], dtype="float32")

Mp = cv2.getPerspectiveTransform(pts, dst)
warped = cv2.warpPerspective(rotated, Mp, (maxWidth, maxHeight))

plt.figure(figsize=(16, 4))
plt.subplot(1, 4, 1); plt.imshow(cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)); plt.title('Foto Asli'); plt.axis('off')
plt.subplot(1, 4, 2); plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)); plt.title('Koreksi Orientasi'); plt.axis('off')
plt.subplot(1, 4, 3); plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)); plt.title('Setelah Cropping'); plt.axis('off')
plt.subplot(1, 4, 4); plt.imshow(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB)); plt.title('Perspective Correction'); plt.axis('off')
plt.tight_layout()
plt.show()