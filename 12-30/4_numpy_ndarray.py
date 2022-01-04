import numpy as np

# np.zeros(배열 형식, 배열 자료형)-> 0으로 설정
array = np.zeros((1280, 1920, 3), np.uint8)

x, y, w, h = 100, 100, 300, 300
roi = array[x:x+w, y:y+h]

print(array.shape)
print(roi.shape)
