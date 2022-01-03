import cv2
import numpy as np

src = cv2.imread('dummy.jpg')
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03)

for i in corners:
    # i = np.uint32(i)
    center = tuple(i[0])
    # cv2.circle(dst, tuple(i[0]), 3, (255, 0, 0), 5)
    # center = int(i[0][0]), int(i[0][1])
    cv2.circle(dst, center, 3, (255, 0, 0), 5)

criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 30, 0)
cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria)

for i in corners:
    # cv2.circle(dst, tuple(i[0]), 3, (0, 0, 255), 5)
    center = tuple(i[0])
    # center = int(i[0][0]), int(i[0][1])
    cv2.circle(dst, center, 3, (255, 0, 0), 5)

cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
