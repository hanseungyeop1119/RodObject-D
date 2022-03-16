import cv2

file_name = '3b59c8a5-f0b031cc.jpg'
image = cv2.imread('../data/images/' + file_name)

resize_image = cv2.resize(image, (224, 244))
# 배열 y, x
# image x,y
cv2.imshow('image', image)
cv2.imshow('resize image', resize_image)
cv2.waitKey(0)