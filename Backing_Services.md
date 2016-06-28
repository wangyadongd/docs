# 第六章 后端支持服务

后端支持服务为开发者提供即买即用的大数据服务，后端支持服务可以按照开发者的用量需求来申请，数十秒钟内即可得到一个高可用的后端支持服务。

使用后端支持服务，需要按需申请后端支持服务实例。

## 通过命令行申请后端支持服务

### 1. 查看后端支持服务

登录 DataFoundry，执行命令行

```
oc get backingservice -n openshift
```

得到 DataFoundry 提供的后端支持服务，示例如下：

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

### 2. 查询后端支持服务的详细信息及套餐

以 MongoDB 为例，执行命令：

```
oc describe backingservice NAME -n openshift
```
参数说明：
- `NAME` ：后端支持服务名称

执行命令：

```
oc describe backingservice MongoDB -n openshift
```

得到 MongoDB 后端支持服务的描述：

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

### 3. 申请后端支持服务实例

执行命令：

```
oc new-backingserviceinstance NAME --backingservice_name=BackingServiceName --planid=BackingServicePlanGuid [options]
```

参数说明：
- `NAME`：后端支持服务实例名称；
- `backingservice_name`：后端支持服务名称；
- `planid`：订购的后端支持服务套餐 id。

以 MongoDB 为例，执行命令：

```
oc new-backingserviceinstance mongodb-demo --backingservice_name=MongoDB --planid=257C6C2B-A376-4551-90E8-82D4E619C852
```

### 4. 查看已申请的后端支持服务实例

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
- `NAME`：已申请的后端支持服务实例名称；
- `SERVICE`：后端支持服务实例所属的后端支持服务名称；
- `PLAN`：申请的后端支持服务实例所选套餐名称；
- `BOUND`：绑定服务的个数；
- `STATUS`：后端支持服务实例状态，可能的状态为：创建中、未绑定、已绑定、删除中。

### 5. 查看已申请的后端支持服务实例详情

执行命令：
```
oc describe backingserviceinstance NAME
```
参数说明：
- `NAME`：后端支持服务实例名称。

以 mongodb-demo 为例，执行命令：

```
oc describe backingserviceinstance mongodb-demo
```

得到 mongodb-demo 后端支持服务实例描述：

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

### 6. 后端支持服务实例与服务绑定

执行命令：
```
  oc bind BackingServiceInstanceName DeployConfigName [options]
```

参数说明：
- `BackingServiceInstanceName`：绑定的后端支持服务实例名称；
- `DeployConfigName`：绑定的服务名称。

以 mongodb-demo 与 RStudio 绑定为例：

执行命令：
```
oc bind mongodb-demo rstudio
```

执行命令，查看后端支持服务实例：

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

可看到 mongodb-demo 已绑定一个服务。

执行命令，查看绑定的服务的详情：

```
Name:		rstudio
Created:	5 weeks ago
Labels:		run=rstudio
Annotations:	openshift.io/deployment.cancelled=5
Latest Version:	9
Selector:	run=rstudio
Replicas:	1
Triggers:	Config
Strategy:	Rolling
Template:
  Labels:	run=rstudio
  Containers:
  rstudio:
    Image:	registry.dataos.io/guestbook/rstudio
    Port:	
    QoS Tier:
      cpu:	BestEffort
      memory:	BestEffort
    Environment Variables:
     VCAP_SERVICES:		{"MongoDB":[{"name":"mongodb-demo","label":"","plan":"ShareandCommon","credentials":{"Host":"dashboard.servicebroker.dataos.io","Name":"a20ad002-1d98-11e6-813a-fa163d0e0615","Password":"382565069e4325e17f7406c61bb69f17","Port":"27017","Uri":"mongodb://c5b787259abb48fc5124e7b87994e4da:382565069e4325e17f7406c61bb69f17@dashboard.servicebroker.dataos.io:27017/a20ad002-1d98-11e6-813a-fa163d0e0615","Username":"c5b787259abb48fc5124e7b87994e4da","Vhost":""}}]}
      BSI_MONGODBDEMO_PORT:	27017
      BSI_MONGODBDEMO_VHOST:	
      BSI_MONGODBDEMO_URI:	mongodb://c5b787259abb48fc5124e7b87994e4da:382565069e4325e17f7406c61bb69f17@dashboard.servicebroker.dataos.io:27017/a20ad002-1d98-11e6-813a-fa163d0e0615
      BSI_MONGODBDEMO_NAME:	a20ad002-1d98-11e6-813a-fa163d0e0615
      BSI_MONGODBDEMO_USERNAME:	c5b787259abb48fc5124e7b87994e4da
      BSI_MONGODBDEMO_PASSWORD:	382565069e4325e17f7406c61bb69f17
      BSI_MONGODBDEMO_HOST:	dashboard.servicebroker.dataos.io
  No volumes.

Deployment #9 (latest):
	Name:		rstudio-9
	Created:	19 minutes ago
	Status:		Complete
	Replicas:	1 current / 1 desired
	Selector:	deployment=rstudio-9,deploymentconfig=rstudio,run=rstudio
	Labels:		openshift.io/deployment-config.name=rstudio,run=rstudio
	Pods Status:	1 Running / 0 Waiting / 0 Succeeded / 0 Failed
Deployment #8:
	Created:	11 days ago
	Status:		Complete
	Replicas:	0 current / 0 desired
Deployment #7:
	Created:	12 days ago
	Status:		Failed
	Replicas:	0 current / 0 desired
Deployment #6:
	Created:	4 weeks ago
	Status:		Complete
	Replicas:	0 current / 0 desired
Deployment #5:
	Created:	4 weeks ago
	Status:		Complete
	Replicas:	0 current / 0 desired
Deployment #4:
	Created:	4 weeks ago
	Status:		Failed
	Replicas:	0 current / 0 desired
Deployment #3:
	Created:	4 weeks ago
	Status:		Complete
	Replicas:	0 current / 0 desired
Deployment #2:
	Created:	4 weeks ago
	Status:		Failed
	Replicas:	0 current / 0 desired
Deployment #1:
	Created:	5 weeks ago
	Status:		Complete
	Replicas:	0 current / 0 desired

Events:
  FirstSeen	LastSeen	Count	From				SubobjectPath	Type		Reason			Message
  ---------	--------	-----	----				-------------	--------	------			-------
  19m		19m		1	{deploymentconfig-controller }			Normal		DeploymentCreated	Created new deployment "rstudio-9" for version 9
  19m		19m		1	{deployment-controller }			Warning		FailedUpdate		Cannot update deployment dangsha/rstudio-9 status to Pending: replicationcontrollers "rstudio-9" cannot be updated: the object has been modified; please apply your changes to the latest version and try again
```

服务的配置详情中，后端支持服务实例环境变量被加入了服务的配置信息中。

环境变量的命名规则：`BSI_$BSINAME_$ENV`

### 7. 后端支持服务实例与服务解绑定

执行命令：

```
oc unbind BackingServiceInstanceName DeployConfigName
```

参数说明：
- `BackingServiceInstanceName`：后端支持服务实例名称；
- `DeployConfigName`：服务名称。

以 mongodb-demo 与 RStudio 解绑为例：

```
oc unbind mongodb-demo rstudio
```

可用 `oc get bsi` 以及 `oc describe dc dcname` 来查询解绑是否成功。

## 通过界面申请后端支持服务