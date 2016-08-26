# ZooKeeper

![](img/ZooKeeper.png)

版本：v3.4.8

ZooKeeper是一个分布式的，开放源码的分布式应用程序协调服务。主要是用来解决分布式应用中经常遇到的一些数据管理问题。

## ZooKeeper后端服务

### 申请ZooKeeper实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### ZooKeeper仪表盘

无

### ZooKeeper实例的环境变量举例

- BSI_ZOOKEEPER_ZOOKEEPERTEST_USERNAME=super
- BSI_ZOOKEEPER_ZOOKEEPERTEST_PASSWORD=7bfee9a5d26c077e9d73f3c21460504
- BSI_ZOOKEEPER_ZOOKEEPERTEST_HOST=sb-vjk2uvnkkwvfk-zk.service-brokers.svc.cluster.local
- BSI_ZOOKEEPER_ZOOKEEPERTEST_PORT=2181

- JSON:

{"ZooKeeper":[{"name":"zookeeper-test","label":"","plan":"standalone","credentials":{"Host":"sb-vjk2uvnkkwvfk-zk.service-brokers.svc.cluster.local","Name":"","Password":"37bfee9a5d26c077e9d73f3c21460504","Port":"2181","Uri":"","Username":"super","Vhost":""}}]}

## 其他文档

官方文档：http://zookeeper.apache.org/

帮助文档：https://zookeeper.apache.org/doc/r3.4.8/

API文档：http://zookeeper.apache.org/doc/r3.4.8/api/index.html



