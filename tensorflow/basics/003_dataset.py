import numpy as np
import tensorflow as tf

with tf.compat.v1.Session() as sess:

    my_data = [
        [0, 1,],
        [2, 3,],
        [4, 5,],
        [6, 7,],
    ]

    slices = tf.data.Dataset.from_tensor_slices(my_data)
    next_item = tf.compat.v1.data.make_one_shot_iterator(slices).get_next()

    while True:
        try:
            print(sess.run(next_item))
        except tf.errors.OutOfRangeError as e:
            #print("OutOfRangeError: {0}".format(e))
            break