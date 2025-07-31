# tree_fingerprint.py
import cv2, numpy as np, hashlib, imagehash, bchlib
from PIL import Image
from pathlib import Path

# ---------- helper: crop & unwrap the disc ----------
def isolate_disc(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    # brute-force: biggest circle
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2,
                               50, param1=100, param2=30,
                               minRadius=50, maxRadius=0)
    if circles is None:
        raise ValueError("No circle found")
    x, y, r = circles[0][0]
    x, y, r = int(x), int(y), int(r)
    crop = img[y-r:y+r, x-r:x+r]
    # unwrap to polar 256×256
    polar = cv2.warpPolar(crop, (256, 256),
                          (r, r), r, cv2.WARP_FILL_OUTLIERS)
    return cv2.cvtColor(polar, cv2.COLOR_BGR2GRAY)

# ---------- helper: 1-D radial profile ----------
def radial_profile(polar):
    return polar.mean(axis=1)            # 256-value vector

# ---------- main: turn image → SHA-256 string ----------
def fingerprint(path):
    img = cv2.imread(str(path))
    polar = isolate_disc(img)
    vec = radial_profile(polar)
    # quantise to 8-bit ints for reproducibility
    q = (vec / vec.max() * 255).astype(np.uint8).tobytes()
    return hashlib.sha256(q).hexdigest()

if __name__ == "__main__":
    for p in Path("same").glob("*.jpg"):
        print(p.name, fingerprint(p))

