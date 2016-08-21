# 第四节：使用 User Provided Service - RStudio

> 本教程基于 DataFoundry 经典界面编写，考虑到产品的快速演进，部分步骤和图示可能已经改变。

## 1 第四节所覆盖的知识点

在第四节，我们将学会如何进行：

- 从公有镜像仓库部署应用
- 自定义后端支持服务实例
- 将应用与自定义后端支持服务绑定

## 2 关于 RStudio 应用

RStudio 是一款免费的编程工具，它运行用户通过 RStudio 直接从源代码编辑器中执行程序和处理多个项目、工作文件夹，同时还提供了大量的图形和统计方法、统计计算和图形，并支持语法高亮、只能缩进、搜索跳转、预览等多种特色！

在本节，我们将演示如何通过 DataFoundry 平台提供的公有镜像部署 RStudio 应用绑定自定义后端支持服务实例。


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


## 4 Step by Step 详细操作

下面分别对图形界面和命令行两种方式进行介绍。

### 4.1 命令行操作

#### Step 1 ：服务部署

1）命令行操作时，“服务部署“可以通过一个命令 `oc run` 完成。

   从 DataFoundry 平台提供的公有镜像部署 RStudio：

```
$ oc run rstudio --image=registry.dataos.io/guestbook/rstudio
  deploymentconfig "rstudio" created
```  

2）查看部署结果：  

```
$ oc get pods
  NAME              READY     STATUS    RESTARTS   AGE
  rstudio-2-24p9b   1/1       Running   0          1m
``` 

     
#### Step 2：自定义后端支持服务实例

1）DataFoundry 提供两种后端支持服务实例创建方式：

- 从后端支持服务市场申请，可参见第二节；
- 自定义创建后端支持服务实例。

2）本节我们学习自定义创建后端支持服务实例：

```   
$ oc new-instance ups-mongodb \
>  -p name=fa2d11bb-024a-11e6-bba3-fa163d0e0615 \
>  -p name=fa2d11bb-024a-11e6-bba3-fa163d0e0615  \
>  -p password=868b3598a084fdd8bbe369249b92f4c9 \
>  -p port=27017 \
>  -p uri=mongodb://741257d996556aecda970644813ebec6:868b3598a084fdd8bbe369249b92f4c9@dashboard.servicebroker.dataos.io:27017/fa2d11bb-024a-11e6-bba3-fa163d0e0615 \
>  -p username=741257d996556aecda970644813ebec6 
User-Provided-Service Instance has been created.
```

3）查看后端服务实例列表：

```   
$ oc get bsi
```

以上命令输出结果为：  

```   
  NAME              SERVICE                 PLAN             BOUND     STATUS
  333c              Spark                   One_Worker       1         Bound
  dangsha890        Mysql                   NoCase           2         Bound
  etcd              ETCD                    standalone       0         Unbound
  fdfd              ETCD                    standalone       1         Bound
  my-mongodb        MongoDB                 ShareandCommon   6         Bound
  mysqlinst         Mysql                   Experimental     2         Bound
  new-spark         Spark                   One_Worker       2         Bound
  postgresqlinst    PostgreSQL              Experimental     2         Bound
  postgresqlinst1   PostgreSQL              Experimental     2         Bound
  postgresqlinst2   PostgreSQL              Experimental     2         Bound
  spark             Spark-v1.5.2            One_Worker       2         Bound
  ups-mongodb       USER-PROVIDED-SERVICE                    0         Unbound

```   

4）查看后端服务实例详细信息：

```
$ oc describe bsi ups-mongodb
  Name:						ups-mongodb
  Created:					5 minutes ago
  Labels:					<none>
  Annotations:				USER-PROVIDED-SERVICE=true
  Status:					Unbound
  DashboardUrl:				<none>
  BackingServiceName:		USER-PROVIDED-SERVICE
  BackingServicePlanName:	<none>
  BackingServicePlanGuid:	USER-PROVIDED-SERVICE
  Parameters:
  Bound:					0
  No events.
```

#### Step 4：后端服务实例绑定

1）以上服务实例创建完成，我们继续把 ups-mongodb 绑定到 RStudio 应用中：

```
$ oc bind ups-mongodb rstudio
  Backing Service Instance has been bound.
```  

2）查看部署结果：

```
$ oc get pods
  NAME              READY     STATUS    RESTARTS   AGE
  rstudio-3-c7t34   1/1       Running   0          1m
```  

3）Pod 已正常启动，给 RStudio 生成一个 route 地址后就可以访问了：

```
$ oc expose dc rstudio  --port=8787 --name=rstudio
$ oc expose svc rstudio --hostname=rstudio.demo.app.dataos.io --name=rstudio
```
