import tensorflow as tf

# Train data set
x_data = [1, 2, 3]
y_data = [1, 2, 3]

# Try to find values for W and b that compute y_data = W * x_data + b
# Weight
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
# Bias
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

# Placeholder
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# Hypothesis (Change x_data to X)
hypothesis = W * X + b

# Simplified cost function(Change y_data to Y)
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize
# Variable 'a' is Learning rate, alpha
a = tf.Variable(0.1)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

# Before starting, initialize the variables.
init = tf.initialize_all_variables()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line
for step in xrange(2001):
	sess.run(train, feed_dict={X:x_data, Y:y_data})
	if step % 20 == 0:
		print step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W), sess.run(b)

# Advantage of Placeholder
print sess.run(hypothesis, feed_dict={X:5})
print sess.run(hypothesis, feed_dict={X:2.5})

