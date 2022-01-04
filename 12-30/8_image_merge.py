import cv2
import numpy as np

one = cv2.imread("./image/one.jpg")
two = cv2.imread("./image/two.jpg")
three = cv2.imread("./image/three.jpg")
four = cv2.imread("./image/four.jpg")

# 높이 20px, 길이는 one, two 가로 길이 만큼 검은색 선 생성
horizontal1 = np.full((20, one.shape[1], 3), [0, 0, 0], dtype=np.uint8)
horizontal2 = np.full((20, two.shape[1], 3), [0, 0, 0], dtype=np.uint8)

# 왼쪽 오른쪽에 이미지 만들기
left = np.vstack((one, horizontal1, three))
right = cv2.vconcat((two, horizontal2, four))

# 중앙선 생성
vertical = np.full((left.shape[0], 50, 3), 0, dtype=np.uint8)

#모든 이미지 병합
dst = cv2.hconcat((left, vertical, right))

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
