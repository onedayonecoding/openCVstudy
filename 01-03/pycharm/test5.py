import cv2
import numpy as np
src = cv2.imread('car.png',cv2.IMREAD_GRAYSCALE)

src = cv2.GaussianBlur(src, (5, 5), 0, 0, borderType=cv2.BORDER_ISOLATED)

dst = cv2.Canny(src, 100, 200, apertureSize=3, L2gradient=True)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
