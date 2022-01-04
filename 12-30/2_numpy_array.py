import numpy as np

# 0~11까지 요소 자동으로 배열 생성
array = np.arange(12)

# z축 2 y축 3, x축 2 3차원 배열로 정렬
reshape1 = array.reshape(2, 3, 2)
print(reshape1)

# 행이 2열인 배열로, Fortran 스타일로 정렬
reshape2 = np.reshape(array, (2, -1), order='F')
print(reshape2)


# 행이 2열인 배열로, C 스타일로 정렬
reshape3 = np.reshape(array, (2, -1), order='C')
print(reshape3)
