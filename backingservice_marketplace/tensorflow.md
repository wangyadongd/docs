# TensorFlow

![](img/TensorFlow.png)

版本：v0.8.0

TensorFlow是谷歌基于DistBelief进行研发的第二代人工智能学习系统。支持异构设备分布式计算，能够在各个平台上自动运行模型，从电话、单个CPU / GPU到成百上千GPU卡组成的分布式系统。

## TensorFlow后端服务

### 申请TensorFlow实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### TensorFlow仪表盘

无

### TensorFlow实例环境变量举例

- BSI_TENSORFLOW_TENSORFLOWTEST_HOST=sb-gcmeyjutjesbe-tnsrflw.service-brokers.svc.cluster.losl

- JSON:

{"TensorFlow":[{"name":"tensorflow-test","label":"","plan":"standalone","credentials":{"Host":"sb-gcmeyjutjesbe-tnsrflw.service-brokers.svc.cluster.local","Name":"","Password":"","Port":"8888","Uri":"","Username":"","Vhost":""}}]}

### 使用TensorFlow实例

TensorFlow 实例与服务绑定后，使用host环境变量连接 TensorFlow 实例。

## 其他文档

官方文档：https://www.tensorflow.org/

帮助文档：https://github.com/tensorflow/tensorflow

中文文档：https://github.com/jikexueyuanwiki/tensorflow-zh
