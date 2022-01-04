import cv2

src = cv2.imread("./image/swan.jpg")
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)

cv2.namedWindow("binary", flags=cv2.WINDOW_FREERATIO)
cv2.resizeWindow("binary", 1024, 600)
cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
