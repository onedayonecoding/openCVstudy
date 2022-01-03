import cv2
import numpy as np

src = cv2.imread('egg.jpg')
data = src.reshape(-1, 3).astype(np.float32)

k = 3
criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TermCriteria_EPS, 10, 0.001)
# 이미지 압축률, 라벨, 중심점 = cv2.kmeans(입력이미지, 군집수, 베스트라벨 저장변수, 기준, 시도횟수, 초기 중심정 선택방법)
retval, bestLabels, centers = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = centers.astype(np.uint8)
dst = centers[bestLabels].reshape(src.shape)

print(centers)
print()
print(centers.shape)
print()
print(bestLabels)

cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
