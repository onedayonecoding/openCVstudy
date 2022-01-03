import cv2
import numpy as np
src = cv2.imread('book.jpg',cv2.IMREAD_GRAYSCALE)

src = cv2.GaussianBlur(src, (5,5),0,0, borderType=cv2.BORDER_ISOLATED)

dx = cv2.Scharr(src,cv2.CV_32F, 1,0, delta = 0)
dy = cv2.Scharr(src,cv2.CV_32F, 0,1, delta = 0)

mag = cv2.magnitude(dx,dy)
mag = np.clip(mag,0,255).astype(np.uint8)

cv2.imshow('src', mag)
cv2.waitKey(0)
cv2.destroyAllWindows()
