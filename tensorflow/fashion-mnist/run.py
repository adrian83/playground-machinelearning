import tensorflow as tf

EPOCHS = 10


fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(class_names))
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=EPOCHS)

#test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
model.evaluate(test_images,  test_labels, verbose=2)

probability_model = tf.keras.Sequential([
    model, 
    tf.keras.layers.Softmax()
])


predictions = probability_model.predict(test_images)

print(str(predictions[:5]))



