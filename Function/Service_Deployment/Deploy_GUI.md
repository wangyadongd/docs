## 通过界面部署服务

### 点击“服务部署”、“新建服务”

![](../img/Deployment1.png)

输入“服务名称”、“创建容器”，配置容器包括：容器名称、镜像名称及版本。如果需要开放端口，可以选择容器要开放的端口。配置信息包括：“端口协议”、“容器端口”、“服务端口”。

DataFoundry支持三种镜像仓库：

* 用户内置镜像仓库：通过 DataFoundry 平台构建的镜像；
* 仓库镜像：registry.dataos.io 中用户自己私有的镜像；
* 镜像中心：镜像中心包含 DataFoundry 官方镜像、Docker 官方镜像的镜像。

![](../img/Deployment_Registry.png)

### 服务高级配置

![](../img/Deployment2.png)

配置服务副本数量、重启策略、路由、选择要绑定的后端服务、配置环境变量。点击创建服务。

### 配置自动部署

可支持两种触发器“镜像变化触发自动部署”、“服务配置变化触发自动部署”。
![](../img/CD.png)
