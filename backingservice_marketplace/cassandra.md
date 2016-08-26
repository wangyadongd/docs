# Cassandra

![](img/Cassandra.png)

版本：v3.4

Cassandra 是一套开源分布式 NoSQL 数据库系统。基于 Column 的结构化，拥有良好的伸展性。

## Cassandra后端服务

### 申请Cassandra实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### Cassandra仪表盘

无

### Cassandra实例环境变量举例

- BSI_CASSANDRA_CASSANDRATEST_USERNAME=757t6hypa6b4c
- BSI_CASSANDRA_CASSANDRATEST_PASSWORD=c78e429cbe32e585abd0e96cbd36387f
- BSI_CASSANDRA_CASSANDRATEST_HOST=sb-iiqzbshe6j4ty-cssndr.service-brokers.svc.cluster.local
- BSI_CASSANDRA_CASSANDRATEST_PORT="9042"

- JSON:

{"Cassandra":[{"name":"cassandra-test","label":"","plan":"standalone","credentials":{"Host":"sb-iiqzbshe6j4ty-cssndr.service-brokers.svc.cluster.local","Name":"","Password":"c78e429cbe32e585abd0e96cbd36387f","Port":"9042","Uri":"","Username":"757t6hypa6b4c","Vhost":""}}]}

### 使用Cassandra实例

Cassandra 实例与服务绑定后，使用host、 port、 username、 password等环境变量连接 Cassandra 实例。

## 其他文档

官方文档：http://cassandra.apache.org/

帮助文档：http://cassandra.apache.org/doc/latest/

API文档:http://datastax.github.io/python-driver/api/
