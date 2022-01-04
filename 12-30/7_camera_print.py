import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)

while True:
    ret, frame = capture.read()
    if (ret == True):
        cv2.imshow("VideoFrame", frame)
        if (cv2.waitKey(33) == ord('q')): break
    else: break
capture.release()
cv2.destroyAllWindows()