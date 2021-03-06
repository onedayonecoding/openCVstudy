import cv2
import numpy as np

def loadTrainData(image_path, label_path):
# open : python 파일 열기 함수 'rb': 바이트 모드로 읽기 as 변수명 : 파일 인스턴스
    with open(image_path, 'rb') as image_data:
        images = np.frombuffer(image_data.read(), dtype=np.uint8, offset=16).reshape(-1, 784)
    with open(label_path, 'rb') as label_data:
        labels = np.frombuffer(label_data.read(), dtype=np.uint8, offset=8)
    return images, labels

train_x, train_y = loadTrainData("./fashion-mnist/train-images-idx3-ubyte", "./fashion-mnist/t10k-labels-idx1-ubyte")
test_x, test_y = loadTrainData("./fashion-mnist/t10k-images-idx3-ubyte", "./fashion-mnist/t10k-labels-idx1-ubyte")

# cv2.imshow('images', train_x[0].reshape(28, 28, 1))
# cv2.waitKey()
# cv2.destroyAllWindows()

knn = cv2.ml.KNearest_create()
knn.train(train_x.astype(np.float32), cv2.ml.ROW_SAMPLE, train_y.astype(np.int32))
count = 500
retval, results, neighborResponses, dist = knn.findNearest(test_x[:count].astype(np.float32), k=7)

for idx, result in enumerate(results):
    print("index : {}".format(idx))
    # print("예측값 : {}".format(label_dict[int(result)]))
    # print("실제값 : {}".format(label_dict[test_y[idx]]))
    cv2.imshow("image", test_x[idx].reshape[28, 28, 1])

    key = cv2.waitKey(0)
    if key == ord('q') or key == 27:
        break
cv2.destroyAllWindows()

