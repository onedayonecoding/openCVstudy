import cv2

src = cv2.imread('dandelion.jpg', cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5), anchor=(-1,-1))
dst = cv2.erode(src,kernel,iterations=3)
dst = cv2.pyrDown(dst)

cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()