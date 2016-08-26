# Redis


![](img/Redis.png)

版本：v2.8

Redis是一个可基于内存亦可持久化的日志型、Key-Value数据库。支持字符串、哈希表、列表、集合、有序集合，位图，hyperloglogs等数据类型。内置复制、Lua脚本、LRU收回、事务以及不同级别磁盘持久化功能。

## Redis后端服务

### 申请Redis实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### Redis仪表盘

无

### Redis实例环境变量举例

- BSI_REDIS_REDISTEST_PASSWORD=8cefc7cb5901b914bf265631f0aa9113
- BSI_REDIS_REDISTEST_HOST=sb-ggmmyzrtthgom-redis.service-brokers.svc.cluster.local
- BSI_REDIS_REDISTEST_PORT="26379"
- BSI_REDIS_REDISTEST_NAME=cluster-sb-ggmmyzrtthgom-redis

- JSON:

{"Redis":[{"name":"redis-test","label":"","plan":"standalone","credentials":{"Host":"sb-ggmmyzrtthgom-redis.service-brokers.svc.cluster.local","Name":"cluster-sb-ggmmyzrtthgom-redis","Password":"8cefc7cb5901b914bf265631f0aa9113","Port":"26379","Uri":"","Username":"","Vhost":""}}]}

### 使用Redis实例

Redis 实例与服务 bind 后，返回的环境变量中， BSI_REDIS_REDISTEST_HOST 是哨兵地址。

Redis 的 Master 的 IP 地址需要通过 BSI_REDIS_REDISTEST_HOST、BSI_REDIS_REDISTEST_PORT、BSI_REDIS_REDISTEST_PASSWORD 查询得到。

然后连接Master。

## 其他文档

官方文档：http://www.redis.net.cn/

官方教程：http://www.redis.net.cn/tutorial/3501.html

API文档:http://redis.io/topics/data-types-intro


