import cv2

src = cv2.imread("./image/crow.jpg")
# 색상 변환 cvtColor(src, 색상code)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.namedWindow("dst", flags=cv2.WINDOW_FREERATIO)
cv2.resizeWindow("dst", 1024, 600)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
