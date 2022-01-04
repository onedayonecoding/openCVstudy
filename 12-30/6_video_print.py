import numpy as np
import cv2
# 동영상 캡처 이미지 설정
capture = cv2.VideoCapture("./image/Star.mp4")

while True:
    #동영상 프레임 설정
    ret, frame = capture.read()

    #동영상 끝까지 갈시 다시 처음으로 롤백
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("./image/Star.mp4")

    cv2.imshow("Video",frame)
    if cv2.waitKey(33) == ord('q'): break

capture.release()
cv2.destroyAllWindows()
