import numpy as np
import cv2

src = cv2.imread("clouds.jpg")
height, width, _ = src.shape

cv2.namedWindow('dst', flags = cv2.WINDOW_NORMAL)
cv2.namedWindow('src', flags = cv2.WINDOW_NORMAL)

cv2.circle(src, (0,0), 10, (255,0,0), 10) # B
cv2.circle(src, (0,height), 10, (0,255,0), 10) # G
cv2.circle(src, (width,0), 10, (0,0,255), 10) # R
cv2.circle(src, (width,height), 10, (0,255,255), 10) # Y

cv2.imshow('src', src)

pts1 = np.float32([[0,0], [0, height], [width, 0], [width, height]])
pts2 = np.float32([[300, 300], [0, height-200], [800, 200], [width - 100, height-100]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(src, matrix, (width, height))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()