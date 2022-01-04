import cv2
import tensorflow as tf
import numpy as np
import re

with open("mscoco_complete_label_map.pbtxt", "rt") as f:
    pb_classes = f.read().rstrip("\n").split("\n")
    classes_label = dict()

    for i in range(0, len(pb_classes), 5):
        pb_classId = int(re.findall("\d+", pb_classes[i + 2])[0])
        pattern = 'display_name: "(.*?)"'
        pb_text = re.search(pattern, pb_classes[i+3])
        classes_label[pb_classId] = pb_text.group(1)


model = tf.saved_model.load("./ssd_mobilenet_v2_320x320_coco17_tpu-8/saved_model")
capture = cv2.VideoCapture("Highland_Cows .mp4")

while True:
    ret, frame = capture.read()

    # 지금 프레임이 마지막 프레임이면 break
    if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)): break
    # 현재 이미지 가 RGB라서 RGB로 변경
    input_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    input_tensor = tf.convert_to_tensor(input_img)
    #tensor 축 추가 [추론할 이미지 수, 높이, 너비, 채널]
    input_tensor = input_tensor[tf.newaxis, ...]

    #모델 추론 및 결과 반환 320 x 320로 알아서 변환
    output_dict = model.signatures["serving_default"](input_tensor)

    #output_dict 사전 형식으로 검출된 객체 클래스, 검출 객체 확률, 검출 객체 사각형등 변환
    classes = output_dict["detection_classes"][0]
    scores = output_dict["detection_scores"][0]
    boxes = output_dict["detection_boxes"][0]

    height, width, _ = frame.shape

    with open ("mscoco_complete_label_map.pbtxt","rt") as f:
        pb_classes = f.read().rstrip("\n").split("\n")

    for idx, score in enumerate(scores):
        if (score > 0.7):
            class_id = int(classes[idx])
            box = boxes[idx]

            x1 = int(box[1] * width)
            y1 = int(box[0] * height)
            x2 = int(box[3] * width)
            y2 = int(box[2] * height)

            cv2.rectangle(frame, (x1, y1), (x2, y2), 255, 1)
            cv2.putText(frame, classes_label[class_id] + ":" + str(float(score)), (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 255, 255), 1)

    cv2.imshow("Object Detector", frame)
    if (cv2.waitKey(33) == ord('q')): break

cv2.destroyAllWindows()
