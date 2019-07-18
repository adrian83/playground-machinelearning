import numpy as np
import tensorflow as tf

with tf.Session() as sess:

    x = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32)
    z = x + y

    print(sess.run(z, feed_dict={x: 3, y: 4.5}))
    print(sess.run(z, feed_dict={x: [1, 3], y: [2, 4]})) 
