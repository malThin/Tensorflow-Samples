import tensorflow as tf
import numpy as np
edge_1 = np.ones([2,2])
edge_2 = np.full([2,2],3)
node_1 = tf.matmul(edge_1, edge_2)
node_2 = tf.add(edge_1, edge_2)
print(node_1)
print(node_2)