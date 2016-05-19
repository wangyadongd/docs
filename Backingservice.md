# 后端支持服务

后端支持服务为开发者提供即开即用的大数据服务，后端支持服务可以按照开发者的用量需求来申请，在申请后端支持服务数十秒钟后即可得到一个高可用的后端支持服务。

## 查询后端支持服务
命令行：

    oc get backingservice -n openshift

查询结果如下：
```
NAME         LABELS                           BINDABLE   STATUS
Cassandra    asiainfo.io/servicebroker=etcd   true       Active
ETCD         asiainfo.io/servicebroker=etcd   true       Active
Greenplum    asiainfo.io/servicebroker=rdb    true       Active
Kafka        asiainfo.io/servicebroker=etcd   true       Active
MongoDB      asiainfo.io/servicebroker=rdb    true       Active
Mysql        asiainfo.io/servicebroker=rdb    true       Active
PostgreSQL   asiainfo.io/servicebroker=rdb    true       Active
RabbitMQ     asiainfo.io/servicebroker=etcd   true       Active
Redis        asiainfo.io/servicebroker=etcd   true       Active
Spark        asiainfo.io/servicebroker=etcd   true       Active
Storm        asiainfo.io/servicebroker=etcd   true       Active
ZooKeeper    asiainfo.io/servicebroker=etcd   true       Active
```

页面方式：

