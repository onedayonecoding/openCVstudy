import cv2
import numpy as np

image = cv2.imread("./image/mountain.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
result = np.zeros((image.shape[0], 256), dtype=np.uint8)
# print(result)
# print(image.shape)
# print(result.shape)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
# print(hist)

for x, y in enumerate(hist):
    cv2.line(result, (int(x), image.shape[0]), (int(x), image.shape[0] - int(y)), 255)

dst = np.hstack([image[:, :, 0], result])
cv2.namedWindow('dst', flags=cv2.WINDOW_NORMAL)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()