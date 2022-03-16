import os
import cv2

file_name = '3b59c8a5-f0b031cc.jpg'
image = cv2.imread('../data/images/' + file_name)

resize_image = cv2.resize(image, (224, 244))

if not os.path.exists('abcd'):
    os.mkdir('abcd')

cv2.imwrite('1.jpg', resize_image)
cv2.imwrite('abcd/1.jpg', resize_image)