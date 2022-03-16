import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
   '../classification_data/',
    image_size=(224, 224),
    label_mode='categorical'
)

data = train_dataset.take(1)

plt.figure(0)
plt.title('data')

for images, labels in data:
    for i in range(16):
        plt.subplot(4, 4, i + 1)
        plt.imshow(images[i].numpy().astype('uint8'))
        plt.title(train_dataset.class_names[np.argmax(labels[i])])
        plt.axis('off')
plt.show()