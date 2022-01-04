import cv2
import numpy as np

src = cv2.imread('./image/crescent.jpg')

dst_bil = cv2.bilateralFilter(src, 100, 33, 11, borderType=cv2.BORDER_ISOLATED)
dst_gauss = cv2.GaussianBlur(src, (7, 7), 0, 0, borderType=cv2.BORDER_ISOLATED)


sharpening_mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
dst_filter2D = cv2.filter2D(src, -1, sharpening_mask)

cv2.namedWindow("dst_bil", flags=cv2.WINDOW_FREERATIO)
cv2.resizeWindow("dst_bil", 600, 480)
cv2.namedWindow("dst_gauss", flags=cv2.WINDOW_FREERATIO)
cv2.resizeWindow("dst_gauss", 600, 480)
cv2.namedWindow("dst_filter2D", flags=cv2.WINDOW_FREERATIO)
cv2.resizeWindow("dst_filter2D", 600, 480)

cv2.imshow("dst_bil", dst_gauss)
cv2.imshow("dst_gauss", dst_bil)
cv2.imshow("dst_filter2D", dst_filter2D)

cv2.waitKey(0)
cv2.destroyAllWindows()
