# Importing the library
import tensorflow as tf

x = tf.constant(4.0)

# Using GradientTape
with tf.GradientTape() as gfg:
    gfg.watch(x)

    # Using nested GradientTape for calculating higher order derivative
    with tf.GradientTape() as gg:
        gg.watch(x)
        y = x * x * x
    # Computing first order gradient
    first_order = gg.gradient(y, x)

# Computing Second order gradient
second_order = gfg.gradient(first_order, x)

# Printing result
print("first_order: ", first_order)
print("second_order: ", second_order)



# import tensorflow as tf
#
# x = tf.matmul([[1]], [[2, 3]])
# print(x)
# print(x.shape)
# print(x.dtype)

#
# import tensorflow as tf
#
# x = tf.Variable(initial_value=3.)
#
# # 在 tf.GradientTape() 的上下文内，所有计算步骤都会被记录以用于求导
# with tf.GradientTape() as tape:
#     tape.watch(x)
#     y = tf.square(x)
#     tape.watch(y)
#
#
#
# # 计算y关于x的导数
# y_grad = tape.gradient(y, x)
#
# print([y, y_grad])
