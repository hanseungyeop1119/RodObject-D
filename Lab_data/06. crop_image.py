import cv2
# 2/7
file_name = '3b59c8a5-f0b031cc.jpg'
image = cv2.imread('../data/images/' + file_name)

crop_image = image[10:1200, 10:1200]

cv2.imshow('image', image)
cv2.imshow('crop image', crop_image)
cv2.waitKey(0)