import tensorflow as tf
# 시각화
# import mtplotlib.pyplot as plt

# 훈련을 위한 데이터
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
   '../classification_data/',
    image_size=(224, 224),
    label_mode='categorical'
)
# take(1) 큰 한 덩어리
# 원-핫 인코딩 one-hot Encoding
data = train_dataset.take(1)
for image, labels in data:
    # image : 문제, labels : 정답
    print(image, labels)
print(train_dataset.class_names)
#print(tf.__version__)