import cv2

src = cv2.imread('image/car.png')

dst = src[280:310, 240:405]
dst = cv2.resize(dst, dsize=(256, 256), interpolation=cv2.INTER_NEAREST)

cv2.imshow("aaa", dst)
cv2.waitKey()
cv2.destroyAllWindows()
