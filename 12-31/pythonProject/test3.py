import numpy as np
import cv2

line =np.array([[3,-1],[1,1]],dtype = np.float32)
answer = np.array([3,2],dtype=np.float32)

success, lu = cv2.solve(line,answer,cv2.DECOMP_LU)
print(lu)
print(success)