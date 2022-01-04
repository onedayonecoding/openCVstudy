import numpy as np

array1 = np.arange(6).reshape(2, 3)
array2 = np.arange(6, 12).reshape(2, 3)

# axis는 축 설정이다
merge1 = np.stack([array1, array2], axis=1)
merge2 = np.stack([array1, array2], axis=2)

print(merge1)
print(merge2)

print("--------- split --------------")
array = np.arange(10).reshape((2, 5))

# np.split(배열, 인덱스, axis=n) 인덱스 크기 만큼 배열 분리
detach1 = np.split(array, 2, axis=0)
# np.split(배열, 섹션, axis=n)
detach2 = np.split(array, [2, 3], axis=1)

print(detach1[0])
print(detach1[1])

print(detach2[0])
print(detach2[1])
print(detach2[2])
