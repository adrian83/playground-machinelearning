import numpy as np
import tensorflow as tf

array_1D = np.array([1.3, 2.6, 4.0, 6.2])
array_2D = np.array([[1.3, 2.6], [4.0, 6.2]])
array_3D = np.array([[[1.3, 2.6], [4.0, 6.2]], [[1.1, 3.5], [5.7, 8.9]]])

arrays = [("Array 1D", array_1D), ("Array 2D", array_2D), ("Array 3D", array_3D)]

with tf.Session() as session:

    print("")
    print("BASIC DATA REGARDING NUMPY ARRAYS")

    for array in arrays:
        print("")
        print(array[0])
        print("Dimention(s): {0}".format(array[1].ndim))
        print("Shape: {0}".format(array[1].shape))
        print("Data type: {0}".format(array[1].dtype))
        print("")

        tensor = tf.convert_to_tensor(array[1], dtype = tf.float64)
        print("Tensor: \n{0}".format(session.run(tensor)))
        print("")

    print("BASIC OPERATIONS ON TENSORFLOW TENSORS")
    print("")

    tensor1 = tf.convert_to_tensor([[1, 2], [3, 4]], dtype = tf.int32)
    tensor2 = tf.convert_to_tensor([[2, 3], [4, 5]], dtype = tf.int32)

    print("Tensor 1: \n{0}\n".format(session.run(tensor1)))
    print("Tensor 2: \n{0}\n".format(session.run(tensor2)))

    result1 = tf.add(tensor1, tensor2)
    print("Sum result: \n{0}\n".format(session.run(result1)))

    result2 = tf.subtract(tensor1, tensor2)
    print("Subtraction result: \n{0}\n".format(session.run(result2)))

    result3 = tf.multiply(tensor1, tensor2)
    print("Multiplication result: \n{0}\n".format(session.run(result3)))
