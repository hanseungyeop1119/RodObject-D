import tensorflow as tf

# model = tf.keras.models.load_model('../models/mymodel.h5')
model = tf.keras.models.load_model('../models/classification_model_trained.h5')
model.summary()