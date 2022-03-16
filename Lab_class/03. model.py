import tensorflow as tf

model = tf.keras.applications.MobileNet(
    input_shape=(244, 244, 3),
    include_top=False,
    weights='imagenet'
)

model.trainable = False

model = tf.keras.Sequential([
    model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(9),
    tf.keras.layers.Softmax()
])

model.summary()
# Output 를 사용 하지 않는다.
# 실험,,
# 했는데 어떤 식으로 함? 어떤 모델을 사용함?

