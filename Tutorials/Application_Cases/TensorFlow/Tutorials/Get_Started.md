## Get_Started：用平面拟合三维数据

一起来了解和运行 TensorFlow!

在开始之前，让我们先看一段使用 Python API 撰写的 TensorFlow 示例代码，让你对将要学习的内容有初步的印象。

这段很短的 Python 程序生成了一些二维数据，然后用一条直线拟合它。

```
# 导入所需要的库
import tensorflow as tf
import numpy as np

# 使用 Numpy 生成假数据（phony data），总共100 个点，y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype(np.float32) 
y_data = x_data * 0.1 + 0.3

# 构造一个线性模型
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
init = tf.initialize_all_variables()

# 启动图
sess = tf.Session()
sess.run(init)

# 拟合直线
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))

# 得到最佳拟合结果 W: [0.1], b: [0.3]
```

代码的第一部分构建了一些数据流图。 TensorFlow 在启动 session 和调用 *run* 函数之前，并没有真正运行任何计算。

### 代码下载
- code: [get_started.py](../Code/get_started.py)
- notebook: [get_started.ipynb](../Notebook/get_started.ipynb)