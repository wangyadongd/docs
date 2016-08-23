# Step 1：导入所需要的库
import tensorflow as tf
import numpy as np

# Step 2：使用 Numpy 生成假数据（phony data），总共100 个点，y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype(np.float32) 
y_data = x_data * 0.1 + 0.3

# Step 3：构造一个线性模型
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# Step 4：最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Step 5：初始化变量
init = tf.initialize_all_variables()

# Step 6：启动图
sess = tf.Session()
sess.run(init)

# Step 7：拟合直线
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))

# 得到最佳拟合结果 W: [0.1], b: [0.3]