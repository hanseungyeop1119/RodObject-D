import cv2
import json

# file_name = '786b3729-acc83d6f.jpg'
# file_name = '3b59c8a5-f0b031cc.jpg'
file_name = 'c1ba5ee6-a7916d65.jpg'
image = cv2.imread('../data/images/' + file_name)

f = open('../data/labels/labels.json')
j = json.load(f)

for l in j:
    if l['name'] == file_name:
        for label in l['labels']:
            if 'box2d' in label:
                x1 = label['box2d']['x1']
                x2 = label['box2d']['x2']
                y1 = label['box2d']['y1']
                y2 = label['box2d']['y2']

                red = (0, 0, 255)
                blue = (255, 0, 0)
                yellow = (0, 255, 255)
                pink = (255, 0, 229)
                green = (0, 255, 0)
                mint = (255, 255, 0)
                purple = (255, 0, 128)
                gold = (0, 128, 128)

                if 'car' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8,
                        color=red,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )
                if 'rider' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8,
                        color=mint,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )
                if 'bike' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8,
                        color=blue,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )
                if 'bus' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8,
                        color=green,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )
                if 'truck' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8,
                        color=yellow,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )
                if 'traffic light' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8,
                        color=pink,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )
                if 'traffic sign' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8,
                        color=purple,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )
                if 'person' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8,
                        color=gold,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )

                if 'car' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (red), 2)
                if 'rider' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (mint), 2)
                if 'bike' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (blue), 2)
                if 'bus' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (green), 2)
                if 'truck' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (yellow), 2)
                if 'traffic light' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (pink), 2)
                if 'traffic sign' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (purple), 2)
                if 'person' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (gold), 2)

cv2.imshow('image', image)
cv2.waitKey(0)
# 'attributes': {'weather': 'clear', 'scene': 'city street', 'timeofday': 'night'},