# Step 1：读取数据
import tensorflow as tf
import time
import numpy
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data", one_hot=True)

print "Training data size: ", mnist.train.num_examples
print "Validating data size: ", mnist.validation.num_examples
print "Testing data size: ", mnist.test.num_examples


# Step 2：建立神经网络
# This is where training samples and labels are fed to the graph.
# These placeholder nodes will be fed a batch of training data at each
# training step using the {feed_dict} argument to the Run() call below.
BATCH_SIZE = 64
EVAL_SIZE = 10000
IMAGE_SIZE = 28
NUM_CHANNELS = 1
NUM_LABELS = 10

x = tf.placeholder(tf.float32, shape=(None, IMAGE_SIZE, IMAGE_SIZE, NUM_CHANNELS))
y_ = tf.placeholder(tf.float32, shape=(None, NUM_LABELS))

# The variables below hold all the trainable weights. 
# Convolutional layers.
conv1_weights = tf.Variable(tf.truncated_normal([5, 5, NUM_CHANNELS, 32], stddev=0.1, seed = 2))
conv1_biases = tf.Variable(tf.zeros([32]))

conv2_weights = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1, seed = 2))
conv2_biases = tf.Variable(tf.constant(0.1, shape=[64]))

# fully connected, depth 512.
fc1_weights = tf.Variable(tf.truncated_normal([IMAGE_SIZE // 4 * IMAGE_SIZE // 4 * 64, 512], stddev=0.1, seed = 2))
fc1_biases = tf.Variable(tf.constant(0.1, shape=[512]))

fc2_weights = tf.Variable(tf.truncated_normal([512, NUM_LABELS], stddev=0.1, seed = 2))
fc2_biases = tf.Variable(tf.constant(0.1, shape=[NUM_LABELS]))

def model(data, train=False):
    """The Model definition."""
    # 2D convolution, with 'SAME' padding (i.e. the output feature map has
    # the same size as the input). Note that {strides} is a 4D array whose
    # shape matches the data layout: [image index, y, x, depth].
    conv = tf.nn.conv2d(data, conv1_weights, strides=[1, 1, 1, 1], padding='SAME')
    # Bias and rectified linear non-linearity.
    relu = tf.nn.relu(tf.nn.bias_add(conv, conv1_biases))
    # Max pooling. The kernel size spec {ksize} also follows the layout of
    # the data. Here we have a pooling window of 2, and a stride of 2.
    pool = tf.nn.max_pool(relu, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    
    conv1 = tf.nn.conv2d(pool, conv2_weights, strides=[1, 1, 1, 1], padding='SAME')
    relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv2_biases))
    pool1 = tf.nn.max_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    
    # Reshape the feature map into a 2D matrix to feed it to the fully connected layers.
    pool_shape = pool1.get_shape().as_list()
    reshape = tf.reshape(pool1, [-1, pool_shape[1] * pool_shape[2] * pool_shape[3]])
    
    # Fully connected layer. Note that the '+' operation automatically broadcasts the biases.
    hidden = tf.nn.relu(tf.matmul(reshape, fc1_weights) + fc1_biases)
    # Add a 50% dropout during training only. Dropout also scales
    # activations such that no rescaling is needed at evaluation time.
    if train: hidden = tf.nn.dropout(hidden, 0.5)
    return tf.nn.softmax(tf.matmul(hidden, fc2_weights) + fc2_biases)

print("Network created!")


# Step 3：建立训练过程
# Predictions for the current training minibatch.
train_y = model(x, True)

# softmax cross entropy loss.
loss = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(train_y, 1e-10, 1.0)))
# L2 regularization for the fully connected parameters.
regularizers = (tf.nn.l2_loss(fc1_weights) + tf.nn.l2_loss(fc1_biases) + 
                tf.nn.l2_loss(fc2_weights) + tf.nn.l2_loss(fc2_biases))
# Add the regularization term to the loss.
loss += 5e-4 * regularizers

# Optimizer: set up a variable that's incremented once per batch and
# controls the learning rate decay.
step = tf.Variable(0)

# Decay once per epoch, using an exponential schedule starting at 0.01.
learning_rate = tf.train.exponential_decay(
    0.01,  # Base learning rate.
    step * BATCH_SIZE,  # Current index into the dataset.
    mnist.train.num_examples,  # Decay step.
    0.95,  # Decay rate.
    staircase=True)

# Use simple momentum for the optimization.
optimizer = tf.train.MomentumOptimizer(learning_rate, 0.9).minimize(loss, global_step=step)

# Training accuracy
train_correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(train_y, 1))
train_accuracy = tf.reduce_mean(tf.cast(train_correct_prediction, tf.float32))
    
# Predictions for the test and validation, which we'll compute less often.
eval_y = model(x, False)
eval_correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(eval_y, 1))
eval_accuracy = tf.reduce_mean(tf.cast(eval_correct_prediction, tf.float32))

print("Training & eval step setup!")


# Step 4：训练模型
# Create a local session to run the training.
start_time = time.time()
ROUNDS = 500

reshaped_test_data = numpy.reshape(mnist.test.images, [-1, 28, 28, 1])
test_label = mnist.test.labels
reshaped_validate_data = numpy.reshape(mnist.validation.images, [-1, 28, 28, 1])
validate_label = mnist.validation.labels

with tf.Session() as sess:
    # Run all the initializers to prepare the trainable parameters.
    tf.initialize_all_variables().run()
    print('Initialized!')
    # Loop through training steps.
    for i in range(ROUNDS):
        # Run the graph and fetch some of the nodes.
        xs, ys = mnist.train.next_batch(BATCH_SIZE)
        reshaped_x = numpy.reshape(xs, [BATCH_SIZE, 28, 28, 1])
        sess.run(optimizer, feed_dict={x: reshaped_x, y_: ys})
        
        if i % 100 == 0:
            elapsed_time = time.time() - start_time
            start_time = time.time()

            validate_acc = sess.run(eval_accuracy, feed_dict={x: reshaped_validate_data, y_:validate_label})
            test_acc = sess.run(eval_accuracy, feed_dict={x: reshaped_test_data, y_:test_label})
            print("After %d training step(s), validation accuracy = %g, test accuracy = %g" %  
                  (i, validate_acc, test_acc))

    test_acc = sess.run(eval_accuracy, feed_dict={x: reshaped_test_data, y_:test_label})
    print("Final accuracy = %g" %  (test_acc))