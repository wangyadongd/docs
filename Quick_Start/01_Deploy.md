##  第一节  Hello WordPress  
### 登录 DataFoundry 平台 

```  
$  oc login https://datafoundry-endpoint.xxx.xxx -u username -p password  
```  

### 创建 WordPress 部署任务  
 
```  
$ oc new-app https://github.com/datafoundry/wordpress.git  
  Found Docker image 10e778c (12 days old) from Docker Hub for "library/php:5.6-apache"

    * An image stream will be created as "php:5.6-apache" that will track the source image
    * A Docker build using source code from https://github.com/datafoundry/wordpress.git will be created
    * The resulting image will be pushed to image stream "wordpress:latest"
    * Every time "php:5.6-apache" changes a new build will be triggered
    * This image will be deployed in deployment config "wordpress"
    * Port 80/tcp will be load balanced by service "wordpress"
    * Other containers can access this service through the hostname "wordpress"
    * WARNING: Image "wordpress" runs as the 'root' user which may noe permitted by your cluster administrator

  Creating resources with lab
    imagestream "php" created
    imagestream "wordpress" created
    buildconfig "wordpress" created
    deploymentconfig "wordpress" created
    service "wordpress" created
  Success
    Build scheduled, use 'oc logs -f bc/wordpress' to track its progress.
    Run 'oc status' to view your app.
  ``` 

其中：  

- `imagestream`，是平台显示私有仓库镜像信息的入口，同时也是平台 CD （持续交付）功能的触发入口；
- `oc` 是 DataFoundry 的命令行控制工具，它提供了对 DataFoundry 的所有控制功能；
- `new-app` 是 DataFoundry 的操作命令，它可以通过后续指定的若干参数完成一个应用的构建和发布；
- `https://github.com/datafoundry/wordpress.git` 是一个 Git 代码仓库，它是我们要在 DataFoundry 发布的第一个应用。

输入命令并点击回车后，命令行会等待一段时间，等待时间的长短与代码仓库的代码量，命令执行位置及 Github 的网络条件有关，这段时间内 oc 会先 clone 代码仓库到本地，对代码仓库中的 Dockerfile 进行解析，主要是获取基础镜像信息。
    
### DataFoundry 的常见基本要素
- `buildconfig`，简写为 bc，用来存储镜像构建所需的配置信息，包括最基本的代码仓库地址、构建分支、Tag、Commit-ID 信息、Dockerfile 位置、镜像构建输出位置及名称，在相对高级的应用场景下还包含 CI （持续集成）出发器，Github Webhook、私有 Git 仓库登录信息等；
- `deployconfig`，简写为 dc，用来存储镜像部署所需的配置信息；
- `service`，简写为svc，是平台提供应用高可用和服务发现功能的入口；
- `imagestream`，简写为is，是平台显示私有仓库镜像信息的入口，同时也是平台 CD 功能的触发入口。  

### 查询基础要素信息  

```  
oc get buildconfig <buildconfig-name>
oc get deployconfig <deployconfig-name>
oc get service <service-name>
oc get imagestream <imagestream-name>
```  
### 　　查询基础要素详情  

```  
oc describe buildconfig <buildconfig-name>  
oc describe deployconfig <deployconfig-name>  
oc describe service <service-name>  
oc describe imagestream <imagestream-name>  
```  
###　　修改基础要素详情   

```  
oc edit buildconfig <buildconfig-name>  
oc edit deployconfig <deployconfig-name>  
oc edit service <service-name>  
oc edit imagestream <imagestream-name>  
```

在简单了解了 DataFoundry 的基本要素后，我们来看看命令执行的结果，这里要特别强调的是 DataFoundry 的命令是异步设计的。绝大多数命令的返回结果仅仅代表系统已经接受到了请求，并不表示相关操作已经完成，也就是说 `oc new-app` 执行成功后只是个开始，我们需要逐个确认每个基本要素的执行情况，只有当所有的基本要素全部完成之后才表示一个应用真正发布成功。

不过也有可能出现 `oc new-app` 命令本身就执行失败或部分失败的问题，大体上有如下几种可能：

* **代码仓库不可达**：因为网络问题或者仓库地址错误或者私有代码仓库密码错误，导致oc命令不能正确clone代码仓库内容  
* **关键基础要素名称重复**：如果平台中已存在相名的基础要素，那么对该基础要素的创建就会失败，当然基础要素创建失败并不代表整个应用发布过程的失败，如果旧的基础要素信息满足要求，则可以继续使用而不用在意执行 `new-app` 过程中出现的错误提示，但如果旧的基础要素信息不符合应用或者服务发布的要求，那么需要删除这些基础要素，基础要素的名称可以通过 `new-app` 的错误提示确定，也可以通过相关要素的查询命令进行查询。

### 删除基础要素

```   
oc delete buildconfig <buildconfig-name>  
oc delete deployconfig <deployconfig-name>  
oc delete service <service-name>  
oc delete imagestream <imagestream-name>  
```  
    
## 通过界面部署 WordPress

1.  登录平台  
  ![](../img/Screenshot from 2016-05-12 18-14-31.png)
  
1. 在左侧菜单中点击“代码构建”  
 ![](../img/Screenshot from 2016-05-17 12-10-38.png)  

1. 点击“新建构建”
  ![](../img/Screenshot from 2016-05-12 18-16-17.png)

1. 输入“构建名称”、“代码 URL ”后，点击“开始构建”
  ![](../img/Screenshot from 2016-05-17 12-11-09.png)

1. 在状态页中可以查看构建状态，构建完成后可以镜像仓库中查看本次构建的镜像，鼠标移动到镜像仓库上后，可以点击“部署最新版本”来部署该镜像
 ![](../img/Screenshot from 2016-05-17 12-21-24.png)

1. 在部署容器镜像时，可填写“服务名称”、“容器名称”、容器启动时占用的端口和对应服务的端口，点击“创建服务”
![](../img/Screenshot from 2016-05-17 12-23-18.png)  

1. 点击“创建服务”后，界面进入“服务详情”页，点击”启动“来触发容器启动
![](../img/Screenshot from 2016-05-17 12-24-07.png) 

1. 在“服务详情”页的“高级配置”区域，可以看到“路由设置”开关，在这里可以为服务配置 route 信息       
![](../img/Screenshot from 2016-05-17 12-25-11.png)

1. 配置完成后，点击“更新”，保存已修改的服务配置
![](../img/Screenshot from 2016-05-17 12-28-18.png)