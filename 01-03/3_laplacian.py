import cv2
import numpy as np
src = cv2.imread('image/book.jpg',cv2.IMREAD_GRAYSCALE)

src = cv2.GaussianBlur(src, (5, 5), 0, 0, borderType=cv2.BORDER_ISOLATED)

laplacian = cv2.Laplacian(src, cv2.CV_8U, ksize=3)
dst = np.zeros(src.shape[:2], np.uint8)
dst[laplacian > 40] = 255

cv2.namedWindow('src', flags=cv2.WINDOW_FREERATIO)
cv2.resizeWindow('src', 1024, 600)
cv2.namedWindow('dst', flags=cv2.WINDOW_FREERATIO)
cv2.resizeWindow('dst', 1024, 600)
cv2.namedWindow('laplacian', flags=cv2.WINDOW_FREERATIO)
cv2.resizeWindow('laplacian', 1024, 600)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('laplacian', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
