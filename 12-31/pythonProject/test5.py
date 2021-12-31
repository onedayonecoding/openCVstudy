import cv2

src = cv2.imread("ferris-wheel.jpg")
dst = src.copy()

for i in range(4):
    dst = cv2.pyrDown(dst)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
