import cv2
import numpy as np


def createImage(lower_mask, upper_mask, threshold):
    complete_mask = cv2.addWeighted(lower_mask, 1.0, upper_mask, 1.0, 0.0)
    dst = cv2.bitwise_and(hsv, hsv, mask=complete_mask)
    dst = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)

    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    binary = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    dst = np.vstack((dst, binary))

    return dst


src = cv2.imread("tomato.jpg")
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)
window_x, window_y = 0, 0

cv2.namedWindow("Palette", flags=cv2.WINDOW_NORMAL)
cv2.createTrackbar("lower_mask_min_value", "Palette", 0, 179, lambda x: x)
cv2.createTrackbar("lower_mask_max_value", "Palette", 5, 179, lambda x: x)
cv2.createTrackbar("upper_mask_min_value", "Palette", 170, 179, lambda x: x)
cv2.createTrackbar("upper_mask_max_value", "Palette", 179, 179, lambda x: x)

cv2.createTrackbar("threshold", "Palette", 127, 255, lambda x: x)

while True:
    lower_mask_min_value = cv2.getTrackbarPos("lower_mask_min_value", "Palette")
    lower_mask_max_value = cv2.getTrackbarPos("lower_mask_max_value", "Palette")

    upper_mask_min_value = cv2.getTrackbarPos("upper_mask_min_value", "Palette")
    upper_mask_max_value = cv2.getTrackbarPos("upper_mask_max_value", "Palette")

    threshold = cv2.getTrackbarPos("threshold", "Palette")

    lower_mask = cv2.inRange(h, lower_mask_min_value, lower_mask_max_value)
    upper_mask = cv2.inRange(h, upper_mask_min_value, upper_mask_max_value)

    cv2.imshow("Palette", createImage(lower_mask, upper_mask, threshold))

    key = cv2.waitKey(33)

    if key == ord('a'):
        window_x -= 10
    elif key == ord('s'):
        window_y += 10
    elif key == ord('w'):
        window_y -= 10
    elif key == ord('d'):
        window_x += 10
    elif key == ord('q') or key == 27:  # 'q' 이거나 'esc' 이면 종료
        break
        cv2.destroyAllWindows()
    cv2.moveWindow("Palette", window_x, window_y)  # 안배움

cv2.destroyAllWindows()
