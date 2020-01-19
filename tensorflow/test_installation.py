#!/usr/bin/env python

import tensorflow as tf

tensor1 = tf.convert_to_tensor([[1, 2], [3, 4]], dtype = tf.int32)
tensor2 = tf.convert_to_tensor([[2, 3], [4, 5]], dtype = tf.int32)

result = tf.add(tensor1, tensor2)

print(result)