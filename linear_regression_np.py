import numpy as np

X_raw = np.array([2013, 2014, 2015, 2016, 2017], dtype=np.float32)
y_raw = np.array([12000, 14000, 15000, 16500, 17500], dtype=np.float32)

X = (X_raw - X_raw.min()) / (X_raw.max() - X_raw.min())
y = (y_raw - y_raw.min()) / (y_raw.max() - y_raw.min())

a, b = 0, 0
y_pred = a * X + b
learning_rate = 1e-3

for _ in range(1000):
    gradient_a, gradient_b = 2 * (y_pred - y).dot(X), 2 * (y_pred - y).sum()
    a = a - learning_rate * gradient_a
    b = b - learning_rate * gradient_b
    y_pred = a * X + b

    loss = np.square(y_pred - y).sum()
    print('a', a, 'b', b, 'loss', loss)
