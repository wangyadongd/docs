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
oc get backingserviceinstance
```
查询结果：
```
NAME           SERVICE        PLAN             BOUND     STATUS
mongodb-demo   MongoDB        ShareandCommon   0         Unbound
my-mongodb     MongoDB        ShareandCommon   3         Bound
my-test-sql    Mysql          Experimental     0         Unbound
mysql-inst1    Mysql          Experimental     0         Unbound
new-mongodb    MongoDB        ShareandCommon   0         Unbound
spark          Spark-v1.5.2   One_Worker       2         Bound
```
内容说明：
1、NAME：已申请的后端支持服务实例名称；
2、SERVICE：后端支持服务实例所属的后端支持服务名称；
3、PLAN：申请的后端支持服务实例所选套餐名称；
4、BOUND：绑定服务的个数；
5、STATUS：后端支持服务实例状态，可能的状态为：创建中、未绑定、已绑定、删除中；

5. 查看已申请的后端支持服务实例详情：
执行命令：
```
oc describe backingserviceinstance NAME
```
参数说明：
NAME：后端支持服务实例名称

以mongodb-demo为例，执行命令：
```
oc describe backingserviceinstance mongodb-demo
```

得到mongodb-demo后端支持服务实例描述：
```
Name:			mongodb-demo
Created:		2 minutes ago
Labels:			<none>
Annotations:		<none>
Status:			Unbound
DashboardUrl:		http://rockmongo-service-broker-db.app.dataos.io/index.php?action=autologin.index&user=66ac2632a7ec0ea0a9480d513539f773&pass=6ba8f37b0a9c914c0bc0adffb37646a7&instance=a20ad002-1d98-11e6-813a-fa163d0e0615
BackingServiceName:	MongoDB
BackingServicePlanName:	ShareandCommon
BackingServicePlanGuid:	257C6C2B-A376-4551-90E8-82D4E619C852
Parameters:
instance_id:	a20ad002-1d98-11e6-813a-fa163d0e0615
Bound:		0
Events:
  FirstSeen	LastSeen	Count	From	SubobjectPath	Type		Reason		Message
  ---------	--------	-----	----	-------------	--------	------		-------
  2m		2m		1	{bsi }			Normal		Provisioning	bsi provisioning done, instanceid: a20ad002-1d98-11e6-813a-fa163d0e0615
```

6. 后端支持服务实例与服务绑定
执行命令：
```
  oc bind BackingServiceInstanceName DeployConfigName [options]
```

参数说明：
BackingServiceInstanceName：绑定的后端支持服务实例名称；
DeployConfigName：绑定的服务名称。

以mongodb-demo与Rstudio绑定为例：
执行命令：
```
oc bind mongodb-demo rstudio
```
绑定结果查询：
执行命令：
```
oc get backingserviceinstance
```

执行结果：
```
NAME           SERVICE        PLAN             BOUND     STATUS
mongodb-demo   MongoDB        ShareandCommon   1         Bound
my-mongodb     MongoDB        ShareandCommon   3         Bound
my-test-sql    Mysql          Experimental     0         Unbound
mysql-inst1    Mysql          Experimental     0         Unbound
new-mongodb    MongoDB        ShareandCommon   0         Unbound
spark          Spark-v1.5.2   One_Worker       2         Bound
```

可看到mongodb-demo已绑定一个服务。



7. 后端支持服务实例与服务解绑定


## 通过界面申请后端支持服务

