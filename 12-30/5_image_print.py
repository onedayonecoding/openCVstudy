import numpy as np
import cv2
# 이미지 설정 cv2.imread(이미지 파일 위치, 이미지 색상 설정)
src = cv2.imread("./image/OpenCV_Logo.png", cv2.IMREAD_GRAYSCALE)

# 창이름 설정
cv2.namedWindow("src", flags=cv2.WINDOW_FREERATIO)
# 창 사이즈 설정
cv2.resizeWindow("src", 400, 200)
# 이미지 출력
cv2.imshow("src", src)
cv2.waitKey(0)
# 모든 윈도우 종료
cv2.destroyAllWindows()
