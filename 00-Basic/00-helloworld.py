import tensorflow as tf

# Create a Constant op
hello = tf.constant('Hello, TensorFlow!')

# Start tf session
sess = tf.Session()

print sess.run(hello)
