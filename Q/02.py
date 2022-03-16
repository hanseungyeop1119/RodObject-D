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

                if 'car' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1,
                        color=red,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )
                if 'bus' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1,
                        color=blue,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )
                if 'truck' in label['category']:
                    cv2.putText(
                        image,
                        text=label['category'],
                        org=(int(x1), int(y1 - 3)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1,
                        color=yellow,
                        thickness=2,
                        lineType=cv2.LINE_AA
                    )
                if 'car' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (red), 4)

                if 'bus' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (blue), 4)

                if 'truck' in label['category']:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (yellow), 4)


cv2.imshow('image', image)
cv2.waitKey(0)