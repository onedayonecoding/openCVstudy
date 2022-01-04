#객체 검출

import re

with open("mscoco_complete_label_map.pbtxt", "rt") as f:
    # test_a = f.read()
    # print(test_a)
    # test_b = f.read().rstrip("\n")
    # print(test_b)
    # 한칸 띄울때 마다 리스트에 저장
    pb_classes = f.read().rstrip("\n").split("\n")
    classes_label = dict()

    for i in range(0, len(pb_classes), 5):
        # 클래스 ID 추출
        pb_classId = int(re.findall("\d+", pb_classes[i + 2])[0])
        
        # .은 줄 바꿈 제외 모든 문자
        # *은 0개 이상
        # ?은 최소한의 매칭
        pattern = 'display_name: "(.*?)"'
        pb_text = re.search(pattern, pb_classes[i+3])
        # print(pb_text)
        # group(i)은 찻으려는 패턴에서 0으로 묶여진 명시적 정규식의 i번째 결과
        classes_label[pb_classId] = pb_text.group(1)
        print(classes_label[pb_classId])
