# 后端支持服务

后端支持服务为开发者提供即开即用的大数据服务，后端支持服务可以按照开发者的用量需求来申请，在申请后端支持服务数十秒钟后即可得到一个高可用的后端支持服务。

使用后端支持服务，需要按需申请后端支持服务实例，

## 通过命令行申请后端支持服务

1. 查看后端支持服务

登录DataFoundry，执行命令行
```
oc get backingservice -n openshift
```

得到DataFoundry提供的后端支持服务，示例如下：
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

2. 查询后端支持服务的详细信息及套餐，以Mongodb为例:
执行命令
```
oc describe backingservice NAME -n openshift
```
参数说明：
NAME：后端支持服务名称

执行命令
```
oc describe backingservice MongoDB -n openshift
```

得到MongoDB后端支持服务的描述：

```
Name:			MongoDB
Created:		10 days ago
Labels:			asiainfo.io/servicebroker=rdb
Annotations:		Class=RDB
Description:		A MongoDB Instance
Status:			Active
Bindable:		true
Updateable:		false
documentationUrl:	https://docs.mongodb.org/manual/
longDescription:	MongoDB unleashes the power of software and data for innovators everywhere
providerDisplayName:	asiainfoLDP
supportUrl:		https://www.mongodb.org/
displayName:		MongoDB
────────────────────
Plan:		Experimental
PlanID:		E28FB3AE-C237-484F-AC9D-FB0A80223F85
PlanDesc:	share a mongodb database in one instance
PlanFree:	true
Bullets:
  20 GB of Disk
  20 connections
PlanCosts:
  CostUnit:	MONTHLY
  Amount:
    eur: 49
    usd: 99
  CostUnit:	1GB of messages over 20GB
  Amount:
    eur: 0.49
    usd: 0.99
────────────────────
Plan:		ShareandCommon
PlanID:		257C6C2B-A376-4551-90E8-82D4E619C852
PlanDesc:	share a mongodb database in one instance,but can select from database aqi_demo
PlanFree:	false
Bullets:
  20 GB of Disk
  20 connections
PlanCosts:
  CostUnit:	MONTHLY
  Amount:
    eur: 49
    usd: 99
  CostUnit:	1GB of messages over 20GB
  Amount:
    eur: 0.49
    usd: 0.99
No events.
```

3. 申请后端支持服务实例:
执行命令：
```
oc new-backingserviceinstance
```
命令说明：
```
Usage:
  oc new-backingserviceinstance NAME --backingservice_name=BackingServiceName --planid=BackingServicePlanGuid [options]
```
参数说明：
NAME：后端支持服务实例名称；
backingservice_name：后端支持服务名称；
planid：订购的后端支持服务套餐id。

以mongodb为例，执行命令：
```
oc new-backingserviceinstance mongodb-demo --backingservice_name=MongoDB --planid=257C6C2B-A376-4551-90E8-82D4E619C852
```

4. 查看已申请的后端支持服务实例：
执行命令：
```
oc describe backingserviceinstance NAME
```
参数说明：
NAME：后端支持服务实例名称



## 通过界面申请后端支持服务

