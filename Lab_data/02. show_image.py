# 1/24
import cv2
class_name = input()
file_name = input()
#file_name = '3b59c8a5-f0b031cc.jpg'
#image = cv2.imread('../data/images/'+class_name + file_name)

# file_name = input()
image = cv2.imread('../classification_data/' + class_name + '/' + file_name)

# 띄우고 나서 바로 꺼짐
cv2.imshow('image', image)
# 0 = 키를 입력 할 때까지 무한 대기
cv2.waitKey(0)