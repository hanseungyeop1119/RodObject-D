import cv2

file_name = '786b3729-acc83d6f.jpg'
image = cv2.imread('../data/images/' + file_name)

cv2.putText(image, 'PYTHON', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), cv2.LINE_AA)

# 띄우고 나서 바로 꺼짐
cv2.imshow('image', image)
# 0 = 키를 입력 할 때까지 무한 대기
cv2.waitKey(0)