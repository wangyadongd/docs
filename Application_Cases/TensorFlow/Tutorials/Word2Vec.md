## word2vec 简介
word2vec 是一种可以进行高效率词嵌套学习的预测模型。

自然语言处理系统通常将词汇作为离散的单一符号，例如 "cat" 一词或可表示为  `Id537`，而 "dog" 一词或可表示为 `Id143`。

### Skip-Gram 模型
Skip-Gram模型通过目标词汇来预测源词汇。如将数据集：

```
the quick brown fox jumped over the lazy dog
```

转换为：

```
(quick, the), (quick, brown), (brown, quick), (brown, fox), ...
```

神经概率化语言模型通常使用[极大似然法](https://en.wikipedia.org/wiki/Maximum_likelihood) (ML) 进行训练，其中通过 [softmax function](https://en.wikipedia.org/wiki/Softmax_function) 来最大化当提供前一个单词 *h* (代表 "history")，后一个单词的概率 ![](../img/vr1.png) (代表 "target")：

![](../img/vr2.png)

这个模型需要多层的迭代。

Skip-Gram 模型为了避免这种情况发生，使用一个二分类器（逻辑回归）在同一个上下文环境里从 *k* 虚构的 ![](../img/rw5.png) (噪声) 单词区分出真正的目标单词 ![](../img/vr1.png)。

从源词汇预测目标词汇模型如图：

 <img src="../img/nce-nplm.png" width = "400"/>

假设用 t 表示上面这个例子中 quick 来预测 the 的训练的单个循环。用 `num_noise` 定义从噪声分布中挑选出来的噪声（相反的）单词的个数，通常使用一元分布，P(w)。为了简单起见，我们就定 `num_noise=1`，用 sheep 选作噪声词。接下来就可以计算每一对观察值和噪声值的损失函数了，每一个执行步骤就可表示为：

![](../img/vr4.png)
 
整个计算过程的目标是通过更新嵌套参数 ![](../img/theta.png) 来逼近目标函数（这个这个例子中就是使目标函数最大化）。为此我们要计算损失函数中嵌套参数 ![](../img/theta.png) 的梯度，比如 ![](../img/vr5.png) 。

当梯度下降的过程中不断地更新参数，对应产生的效果就是不断地移动每个单词的嵌套向量，直到可以把真实单词和噪声单词很好得区分开。

<img src="../img/linear-relationships.png" width = "600"/>

### 建立图形
先来定义一个嵌套参数矩阵。我们用唯一的随机值来初始化这个大矩阵。对噪声-比对的损失计算就使用一个逻辑回归模型。对此，我们需要对语料库中的每个单词定义一个权重值和偏差值。(也可称之为 **输出权重** 与之对应的 **输入嵌套值**)。

Skip-Gram 模型有两个输入。一个是一组用整型表示的上下文单词，另一个是目标单词。
对批数据中的单词建立嵌套向量，TensorFlow 提供了方便的工具函数。

```
embed = tf.nn.embedding_lookup(embeddings, train_inputs)
```

接下来就是使用噪声-比对的训练方式来预测目标单词：

```
loss = tf.reduce_mean(
  tf.nn.nce_loss(nce_weights, nce_biases, embed, train_labels,
                 num_sampled, vocabulary_size))
```


### 嵌套学习结果可视化
计算相应梯度和更新参数的节点，最后结果如图：

![](../img/tsne.png)

### 代码下载
- code: [word2vec.py](../Code/word2vec.py)
- notebook: [word2vec.ipynb](../Notebook/word2vec.ipynb)