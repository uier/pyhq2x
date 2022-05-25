import cv2
import sys

infile = sys.argv[1]
img = cv2.imread(infile)
w, h = img.shape[:2]

for r in range(h):
    for c in range(w):
        print(img[r][c], end='\t')
    print()