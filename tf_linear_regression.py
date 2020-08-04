import numpy as np
import tensorflow as tf

X_raw = np.array([2013, 2014, 2015, 2016, 2017], dtype=np.float32)
y_raw = np.array([12000, 14000, 15000, 16500, 17500], dtype=np.float32)

X_STD = (X_raw - X_raw.min()) / (X_raw.max() - X_raw.min())
y_STD = (y_raw - y_raw.min()) / (y_raw.max() - y_raw.min())

X = tf.constant(X_STD)
y = tf.constant(y_STD)

a = tf.Variable(initial_value=0.)
b = tf.Variable(initial_value=0.)
variables = [a, b]
optimizer = tf.keras.optimizers.SGD(learning_rate=1e-3)
for _ in range(1000):
    with tf.GradientTape() as tape:
        y_pred = a * X + b
        loss = tf.reduce_sum(tf.square(y_pred - y))

    grads = tape.gradient(loss, variables)

    print('a', a, 'b', b, 'loss', loss)

    optimizer.apply_gradients(grads_and_vars=zip(grads, variables))
