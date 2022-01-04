import cv2

#  이미지 반환 함수
def createImage(h_red):
    dst = cv2.bitwise_and(hsv, hsv, mask=h_red)
    # hsv 이미지와 hsv 이미지를 bitwise_and 연산 할것임, 연산 결과는 dst 변수에 담김
    # bitwise_and 연산의 마스크는 h_red (and 연산 할 부분)

    dst = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)
    # hsv 연산이 끝난 이미지를 BGR 채널 이미지로 변경함
    return dst # 이미지 반환


src = cv2.imread("./image/tomato.jpg")  # 이미지 가져옴
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 색상 검출을 위해 HSV 채널로 변환

h, s, v = cv2.split(hsv)  # hue값 쓰기 위해 hsv 채널 이미지를 분리함

# Palette 이름의 윈도우(창) 생성
cv2.namedWindow("Palette", flags=cv2.WINDOW_FREERATIO)
cv2.resizeWindow("Palette", 1024, 600)

# Palette 윈도우에 Hue 이름의 트랙바 생성, 최소값 0, 최대값 179, lambda x:x 이건 뭐지? -> 아무것도 안하는거
cv2.createTrackbar("Hue", "Palette", 0, 179, lambda x: x)

while True:
    # Palette 윈도우의 Hue 트랙바 움직일 때마다 값을 가져옴
    hue_val = cv2.getTrackbarPos("Hue", "Palette")

    h_red = cv2.inRange(h, 0, hue_val) # hue_val 사용하여 h_red 마스크 생성

    cv2.imshow("Palette", createImage(h_red)) # Palette 윈도우에 createImage 함수 반환 결과(이미지)를 보여줌

    if cv2.waitKey(33) & 0xFF == ord('q'): # 33미리세컨드마다 키입력 대기, q입력 받으면 종료
        break

cv2.destroyAllWindows()  # 모든 윈도우 release(메모리 헤제)