import cv2
import numpy as np

img = np.zeros((3, 3, 3), np.uint8)
img[0][0], img[0][1], img[0][2] = [255, 255, 255], [0, 0, 0], [255, 255, 255]
img[1][0], img[1][1], img[1][2] = [0, 0, 0], [0, 0, 0], [0, 0, 0]
img[2][0], img[2][1], img[2][2] = [255, 255, 255], [0, 0, 0], [255, 255, 255]

cv2.imwrite('demo-4.png', img)


LIGHT_BLUE = [247, 221, 47]
MID___BLUE = [232, 124, 35]
DARK__BLUE = [107, 52, 7]

img = np.array([
    [LIGHT_BLUE, MID___BLUE, MID___BLUE, DARK__BLUE, DARK__BLUE],
    [MID___BLUE, MID___BLUE, DARK__BLUE, DARK__BLUE, DARK__BLUE],
    [MID___BLUE, DARK__BLUE, LIGHT_BLUE, DARK__BLUE, MID___BLUE],
    [MID___BLUE, LIGHT_BLUE, DARK__BLUE, MID___BLUE, MID___BLUE],
    [LIGHT_BLUE, LIGHT_BLUE, MID___BLUE, LIGHT_BLUE, LIGHT_BLUE],
])

cv2.imwrite('demo-5.png', img)


DARK__GREEN = [40, 148, 10]
LIGHT_GREEN = [50, 189, 11]
TREE__BROWN = [19, 38, 69]
GROUNDGREEN = [30, 46, 14]
SKY____BLUE = [227, 218, 184]

img = np.array([
    [DARK__GREEN, LIGHT_GREEN, LIGHT_GREEN, DARK__GREEN, LIGHT_GREEN],
    [LIGHT_GREEN, TREE__BROWN, DARK__GREEN, TREE__BROWN, DARK__GREEN],
    [SKY____BLUE, TREE__BROWN, TREE__BROWN, TREE__BROWN, SKY____BLUE],
    [SKY____BLUE, SKY____BLUE, TREE__BROWN, SKY____BLUE, SKY____BLUE],
    [GROUNDGREEN, GROUNDGREEN, TREE__BROWN, GROUNDGREEN, GROUNDGREEN],
])

cv2.imwrite('demo-6.png', img)


img = np.zeros((3, 3, 3), np.uint8)
img = np.array([
    [LIGHT_BLUE, LIGHT_BLUE, DARK__BLUE],
    [LIGHT_BLUE, LIGHT_BLUE, DARK__BLUE],
    [DARK__BLUE, DARK__BLUE, DARK__BLUE],
])

cv2.imwrite('demo-7.png', img)

