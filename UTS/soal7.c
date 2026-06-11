import cv2
import numpy as np
import imutils

# ======================================
# Membaca gambar
# ======================================
img = cv2.imread("dokumen.jpeg")

if img is None:
    print("Gambar tidak ditemukan!")
    exit()

orig = img.copy()

# ======================================
# Preprocessing
# ======================================
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

edged = cv2.Canny(blur, 75, 200)

gray = cv2.convertScaleAbs(gray, alpha=1.2, beta=30)
# ======================================
# Mencari contour dokumen
# ======================================
cnts = cv2.findContours(
    edged.copy(),
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_SIMPLE
)

cnts = imutils.grab_contours(cnts)

cnts = sorted(
    cnts,
    key=cv2.contourArea,
    reverse=True
)[:5]

docCnt = None

for c in cnts:

    peri = cv2.arcLength(c, True)

    approx = cv2.approxPolyDP(
        c,
        0.02 * peri,
        True
    )

    if len(approx) == 4:
        docCnt = approx
        break

# ======================================
# Fungsi urut titik
# ======================================
def order_points(points):

    rect = np.zeros((4, 2), dtype="float32")

    s = points.sum(axis=1)

    rect[0] = points[np.argmin(s)]
    rect[2] = points[np.argmax(s)]

    diff = np.diff(points, axis=1)

    rect[1] = points[np.argmin(diff)]
    rect[3] = points[np.argmax(diff)]

    return rect

# ======================================
# Perspective Transform
# ======================================
if docCnt is not None:

    document_points = docCnt.reshape(4, 2)

    ordered_rect = order_points(document_points)

    (tl, tr, br, bl) = ordered_rect

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)

    maxWidth = int(
        max(float(widthA), float(widthB))
    )

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)

    maxHeight = int(
        max(float(heightA), float(heightB))
    )

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(
        ordered_rect,
        dst
    )

    warped = cv2.warpPerspective(
        orig,
        M,
        (maxWidth, maxHeight)
    )

    # ======================================
    # Efek scanner hitam putih
    # ======================================
    warped_gray = cv2.cvtColor(
        warped,
        cv2.COLOR_BGR2GRAY
    )

    scanned = cv2.adaptiveThreshold(
        warped_gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # ======================================
    # Simpan hasil
    # ======================================
    cv2.imwrite(
        "hasil_scan_nota.png",
        scanned
    )

    print("Hasil scan berhasil disimpan!")

    # ======================================
    # Menampilkan hasil
    # ======================================
    cv2.imshow("Original", img)
    cv2.namedWindow("Scanner Result", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Scanner Result", 800, 600)
    cv2.imshow("Scanner Result", scanned)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

else:
    print("Dokumen tidak terdeteksi!")