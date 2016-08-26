# Kafka

![](img/Kafka.png)


版本：v0.9.0

Kafka是一种高吞吐量的分布式发布订阅消息系统。通过O(1)的磁盘数据结构提供消息的持久化，此结构对于消息存储能够保持长时间的稳定性能。

## Kafka 后端服务

### 申请 Kafka 实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### Kafka 仪表盘

无

### Kafka 实例环境变量举例

- BSI_KAFKA_KAFKATEST_HOST=sb-dkguni6rnc2fu-kafka.service-brokers.svc.cluster.local
- BSI_KAFKA_KAFKATEST_PORT="9092"
- BSI_KAFKA_KAFKATEST_URI='kafka: sb-dkguni6rnc2fu-kafka.service-brokers.svc.cluster.local:9092 zookeeper: sb-dkguni6rnc2fu-zk.service-brokers.svc.cluster.local:2181 (SuperUser: super, Password: ad56a706c72b1e95f4999d7f84802f12)'

- JSON:

{"Kafka":[{"name":"kafka-test","label":"","plan":"standalone","credentials":{"Host":"sb-dkguni6rnc2fu-kafka.service-brokers.svc.cluster.local","Name":"","Password":"","Port":"9092","Uri":"kafka:          sb-dkguni6rnc2fu-kafka.service-brokers.svc.cluster.local:9092 zookeeper: sb-dkguni6rnc2fu-zk.service-brokers.svc.cluster.local:2181 (SuperUser:
            super, Password: ad56a706c72b1e95f4999d7f84802f12)","Username":"","Vhost":""}}]}

### 使用 Kafka 实例

使用 Kafka 实例与服务绑定返回的 kafka uri 和 zooeeper uri 连接 kafka。

## 其他文档

官方文档：http://kafka.apache.org/

帮助文档：http://kafka.apache.org/documentation.html

API文档:http://kafka.apache.org/documentation.html#api


