import numpy as np
import tensorflow as tf

tf.compat.v1.disable_eager_execution()

x = tf.compat.v1.placeholder(tf.float32)
y = tf.compat.v1.placeholder(tf.float32)
z = x + y


with tf.compat.v1.Session() as sess:

    print(sess.run(z, feed_dict={x: 3, y: 4.5}))
    print(sess.run(z, feed_dict={x: [1, 3], y: [2, 4]})) 

