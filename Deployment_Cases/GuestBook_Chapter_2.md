# 第二节：使用后端服务 - WordPress

> 本教程基于 DataFoundry 经典界面编写，考虑到产品的快速演进，部分步骤和图示可能已经改变。

## 1 第二节所覆盖的知识点

在第二节，我们将学会如何进行：

- 后端服务申请
- 将应用与后端服务绑定

## 2 关于 WordPress 应用

WordPress 是一种使用 PHP 语言开发的博客平台，用户可以在支持 PHP 和 MySQL 数据库的服务器上架设属于自己的网站。也可以把 WordPress 当作一个内容管理系统（CMS）来使用。

在本节，我们将分别使用图形界面与命令行两种方式演示如何通过 DataFoundry 平台提供的 MySQL 后端服务来部署 WordPress 应用。当你看到如下界面，说明 WordPress 应用已经成功运行。

![](img/WordPress.png)

## 3 开始前的准备工作

在你开始之前，你需要在 DataFoundry 注册一个帐号。

对于图形界面操作，你还需要以下浏览器之一：

- Firefox 15 或以上
- Chrome 21 或以上
- Internet Explorer 10 或以上
- Safari 7 或以上

对于命令行操作，你还需要下载 OpenShift 客户端：

- [Linux 32bit](https://s3.cn-north-1.amazonaws.com.cn/datafoundry/client/linux-32bit.tar.gz)
- [Linux 64bit](https://s3.cn-north-1.amazonaws.com.cn/datafoundry/client/linux-64bit.tar.gz)
- [Mac](https://s3.cn-north-1.amazonaws.com.cn/datafoundry/client/mac.zip)
- [Windows](https://s3.cn-north-1.amazonaws.com.cn/datafoundry/client/windows.zip)

Fork WordPress 源码到自己的代码仓库：

- 预置 dockerfile 版，[https://github.com/DataFoundry/wordpress](https://github.com/DataFoundry/wordpress)

## 4 Step by Step 详细操作

下面分别对图形界面和命令行两种方式进行介绍。

### 4.1 图形界面操作

#### Step 1：代码构建

1）登录平台：
![](img/login.png)

2）在左侧菜单中点击“代码构建”、“新建构建”：
![](img/new_build.png)

3）在“构建名称”中输入“wordpress”，在“代码 URL”中选择 GitHub，并选择相应项目和代码分支：
![](img/new_build_detail.png)

4）点击“开始构建” ，可以看到构建记录和日志：
![](img/start_build.png)

注意：
- 为了能够让 WordPress 自动适配后端服务提供的环境变量，我们对 DockerHub 官方 WordPress 镜像进行了微调；
- 在状态页中可以查看构建状态，构建完成后可以镜像仓库中查看本次构建的镜像。

#### Step 2：后端服务申请
1）点击“后端服务”，可以看到目前 DataFoundry 所能提供的各类后端服务：
![](img/backing_service.png)

2）点击“申请实例”，填入“服务名称”，在选择“服务套餐”后点击“创建” ：
![](img/apply_instance.png)

3）后端服务创建完成后，可以显示创建后端服务详细信息：
![](img/service_detail.png)

4）回到“后端服务”，点击“我的后端服务实例”Tab 页，在这里可以看到所有已创建的后端服务实例：
![](img/my_instance.png)
 
#### Step 3：服务部署
1）在左侧菜单栏点击“镜像仓库”，鼠标移动到镜像仓库上后，可以点击“部署最新版本”来部署该镜像： 
![](img/deploy_latest.png)

2）在部署容器镜像时，可填写“服务名称”、“容器名称”、容器启动时占用的端口和对应服务的端口，点击“创建服务”：
![](img/service_deployment.png)

3）在“服务详情”页的“高级配置”区域，可以看到“路由设置”开关，在这里可以为服务配置 route 信息：
![](img/route2.png)

#### Step 4：后端服务绑定
1）最后，在“高级配置”区域，进行“后端服务绑定”与“环境变量设置”：
![](img/service_binding.png)

2）配置完成后，点击“创建服务”，数十秒内即可完成绑定了后端服务的服务部署。部署完成后，点击“路由 URL”下方的 URL，即可访问你所部署的服务：
![](img/deploy_succeed.png)

注意：
- 对于“Step 2：后端服务申请”和“Step 3：服务部署”，你也可以选择先进行“Step 3：服务部署”，再进行“Step 2 & 4：后端服务的申请和绑定”。不过，由于“服务部署”时没有提供后端服务，WordPress 会一直重启；
- 待后端服务创建完成后，在“后端服务”-“我的后端服务实例”Tab 页，选择相应后端服务，点击“服务绑定”按钮，在窗口中点击“新增绑定”，在弹出窗口中选择需要绑定后端服务的应用，后端服务与应用即绑定完成。


### 4.2 命令行操作

命令行操作时，必须先部署服务，再将后端服务与应用绑定，于是我们将操作步骤的顺序略作调整为 1、3、2、4。

#### Step 1 & 3：代码构建+服务部署

1）命令行操作时，“代码构建”和“服务部署”可以通过一个命令 `oc new-app` 完成：

```
$ oc new-app https://github.com/datafoundry/wordpress.git
--> Found Docker image 10e778c (12 days old) from Docker Hub for "library/php:5.6-apache"
    * An image stream will be created as "php:5.6-apache" that will track the source image
    * A Docker build using source code from https://github.com/datafoundry/wordpress.git will be created
      * The resulting image will be pushed to image stream "wordpress:latest"
      * Every time "php:5.6-apache" changes a new build will be triggered
    * This image will be deployed in deployment config "wordpress"
    * Port 80/tcp will be load balanced by service "wordpress"
      * Other containers can access this service through the hostname "wordpress"
    * WARNING: Image "wordpress" runs as the 'root' user which may not be permitted by your cluster administrator
--> Creating resources with label app=wordpress ...
    imagestream "php" created
    imagestream "wordpress" created
    buildconfig "wordpress" created
    deploymentconfig "wordpress" created
    service "wordpress" created
--> Success
    Build scheduled, use 'oc logs -f bc/wordpress' to track its progress.
    Run 'oc status' to view your app.
```  

2）查看部署结果：  

```
$ oc get pods
  NAME                 READY     STATUS             RESTARTS   AGE
  wordpress-1-build    0/1       Completed          0          3m
  wordpress-1-deploy   1/1       Running            0          1m
  wordpress-1-hfzhs    0/1       CrashLoopBackOff   3          1m
``` 

因为没有提供 MySQL 后端服务，WordPress 一直在重启，我们现在来创建 MySQL Backing Service。
     
##### Step 2：后端服务申请

1）在通过 DataFoundry 生成一个 MySQL 的后端服务之前，我们可以先查看一下目前 DataFoundry 已经集成的后端服务。

```   
$ oc get bs -n openshift  
```

注意：   
- 后端服务是 DataFoundry 的特有功能，所以必须要使用 DataFoundry 客户端连接服务端查看；   
- 在查看 DataFoundry 已集成的后端时，要添加后端服务默认的集成命名空间 OpenShift。

以上命令输出结果为：  

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

可以看到 DataFoundry 已集成了非常丰富的后端服务组件，下面我们创建一个 MySQL 后端服务实例。  
  
2）在创建实例之前，我们要先通过 `oc describe bs <backingservcie-name> ` 获取应用所需的后端服务计划（Plan），例如我们获取 MySQL 后端服务的服务计划为：

```   
$ oc describe bs Mysql -n openshift
  Name:					Mysql
  Created:				21 hours ago
  Labels:				asiainfo.io/servicebroker=rdb
  Annotations:			<none>
  Description:			A MYSQL DataBase
  Status:				Active
  Bindable:				true
  Updateable:			false
  documentationUrl:		http://docs.mysql.com
  longDescription:		OpenSoure RDMBS Mysql
  providerDisplayName:	asiainfoLDP
  supportUrl:			http://www.mysql.com
  displayName:			Mysql
────────────────────
  Plan:					Experimental
  PlanID:				56660431-6032-43D0-A114-FFA3BF521B66
  PlanDesc:				share a mysql database in one instance
  PlanFree:				true
  Bullets:
  	20 GB of Disk
  	20 connections
  PlanCosts:
  CostUnit:				MONTHLY
  Amount:
    eur: 49
    usd: 99
  CostUnit:				1GB of messages over 20GB
  Amount:
    eur: 0.49
    usd: 0.99
```

3）我们选取 Experimental 计划创建 MySQL 后端服务实例：

```   
$ oc new-backingserviceinstance mysql-inst1 \
  --backingservice_name=Mysql \
  --planid=56660431-6032-43D0-A114-FFA3BF521B66
  Backing Service Instance has been created.
```

4）查看后端服务列表：

```   
$ oc get bsi
  NAME          SERVICE   PLAN           BOUND     STATUS
  mysql-inst1   Mysql     Experimental   0         Unbound 
```

5）查看后端服务详细信息：

```
$ oc describe bsi mysql-inst1
  Name:						mysql-inst1
  Created:					5 minutes ago
  Labels:					<none>
  Annotations:				<none>
  Status:					Unbound
  DashboardUrl:				http://e412377c9b5f3db:1394e5f077d1519@phpmyadmin-service-broker-db.app.dataos.io?db=8c60f229ef4dac0
  BackingServiceName:		Mysql
  BackingServicePlanName:	Experimental
  BackingServicePlanGuid:	56660431-6032-43D0-A114-FFA3BF521B66
  Parameters:
  instance_id:				340082e4-1734-11e6-a653-fa163edcfb45
  Bound:					0
  Events:
  FirstSeen	LastSeen	Count	From	SubobjectPath	Type	Reason			Message
  ---------	--------	-----	----	-------------	----	------			-------
  5m		5m			1		{bsi}					Normal	Provisioning	bsi provisioning done, instanceid: 340082e4-1734-11e6-a653-fa163edcfb45
```

##### Step 4：后端服务绑定

1）以上服务实例创建完成，我们继续把 MySQL Backing Service 绑定到 WordPress 应用中：

```
$ oc bind mysql-inst1 wordpress
$ oc env dc/wordpress MYSQLBSI=MYSQLINST1 BSITYPE=MYSQL
```  

2）查看部署结果：

```
$ oc get pods
  NAME                READY     STATUS      RESTARTS   AGE
  wordpress-1-build   0/1       Completed   0          7m 
  wordpress-2-55q5a   1/1       Running     0          41s
```  

3）Pod 已正常启动，给 WordPress 生成一个 route 地址后就可以访问了：

```
$ oc expose dc wordpress  --port=80 --name=wordpress
$ oc expose svc wordpress --hostname=wordpress.demo.app.dataos.io --name=wordpress
```