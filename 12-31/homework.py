import cv2
import numpy as np

src = cv2.imread('tomato.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)
h_red = cv2.inRange(h, 0, 5)
a = cv2.inRange(0, 0, 0)

lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
upper_red = cv2.inRange(hsv, (170, 100, 100), (179, 255, 255))

def createImage():
    color = cv2.bitwise_and(hsv, hsv, mask=h_red)
    color2 = cv2.bitwise_and(hsv, hsv, mask=a)
    color = cv2.cvtColor(color, cv2.COLOR_HSV2BGR)

    _, binary = cv2.threshold(color2, 127, 255, cv2.THRESH_BINARY)

    color = cv2.resize(color, dsize=(1440, 200), interpolation=cv2.INTER_AREA)
    binary = cv2.resize(binary, dsize=(1440, 200), interpolation=cv2.INTER_AREA)

    dst = cv2.vconcat([color, binary])
    # hsv 연산이 끝난 이미지를 BGR 채널 이미지로 변경함
    return dst # 이미지 반환

cv2.namedWindow("Palette")
cv2.createTrackbar("lower_hue", "Palette", 0, 5, lambda x: x)
cv2.createTrackbar("lower_hue", "Palette", 0, 5, lambda x: x)
cv2.createTrackbar("upper_hue", "Palette", 170, 179, lambda x: x)
cv2.createTrackbar("upper_hue", "Palette", 170, 179, lambda x: x)
cv2.createTrackbar("threshold", "Palette", 0, 179, lambda x: x)
x,y=0,0
while True:
    # Palette 윈도우의 Hue 트랙바 움직일 때마다 값을 가져옴
    lower_red = cv2.getTrackbarPos("lower_hue", "Palette")
    upper_red = cv2.getTrackbarPos("lower_hue", "Palette")
    aa = cv2.getTrackbarPos("upper_hue", "Palette")
    bb = cv2.getTrackbarPos("upper_hue", "Palette")
    threshold = cv2.getTrackbarPos("threshold", "Palette")

    h_red = cv2.inRange(h, 0, lower_red) # hue_val 사용하여 h_red 마스크 생성
    a = cv2.inRange(h, 0, threshold)  # hue_val 사용하여 h_red 마스크 생성

    cv2.imshow("Palette", createImage()) # Palette 윈도우에 createImage 함수 반환 결과(이미지)를 보여

    key = cv2.waitKey(33)

    if key == ord('a'):
        x -= 100
    elif key  == ord('w'):
        y -= 100
    elif key == ord('s'):
        y += 100
    elif key == ord('d'):
        x += 100
    elif key == ord('q'):  # 33미리세컨드마다 키입력 대기, q입력 받으면 종료
        break

    cv2.moveWindow("Palette", x, y)

cv2.waitKey()
cv2.destroyAllWindows()
