# 第一章 核心概念

DataFoundry 是专注于大数据领域的 PaaS 云平台， 基于 Docker 容器技术，为各类开发者提供云端大数据应用构建、交付和运维服务，并提供应用生命周期全流程、标准化的持续集成、镜像构建、持续交付和自动运维服务。

DataFoundry 整合了亚信在大数据领域潜心耕耘十余年沉淀的大数据服务、应用、算法和解决方案等能力，同时引入第三方服务，可实现快速交付大数据应用、快速搭建并运维大数据平台。

DataFoundry 打造以大数据应用为中心的云计算平台，通过优化开发运维环节、降低 IT 成本，提高了大数据应用和变现的效率，使得原本无法支撑的市场能够进入，使得原本无法成立的商业模式能够实现。

本节将为 DataFoundry 使用者提供应用生命周期中所需的核心概念。
    
## 容器（Containers）

Linux 容器技术提供轻量级的虚拟化设备，以便隔离进程、文件系统和网络等资源。

容器是 DataFoundry 定义的最小的应用运行单元。

DataFoundry 基于 Docker 容器，而 Docker 容器是基于 Docker 镜像（Images）的应用运行单元。
    
## 构建（Builds）

DataFoundry 支持 Docker Build，即以 Dockerfile、源代码为输入，构建出的以可运行的镜像为输出的过程。

DataFoundry 支持以 Git 协议为基础的代码仓库，如 Github、GitLab。
    
## 镜像（Images）
    
DataFoundry 的镜像指 Docker 镜像，它是 Docker 容器的基础。Docker 镜像根据 Dockerfile 的定义将应用程序及其依赖打包为一个单独的虚拟容器，这个容器可运行在任何 Linux 服务器上。这大大提高了程序运行的灵活性和可移植性，无论是否需要许可、是公有云抑或私有云、是否为裸机环境等。
    
## 镜像仓库（Image Registry）
    
镜像仓库用于接收及存储 DataFoundry 上的 Docker 镜像。镜像仓库存储了每次构建成功的镜像，并以镜像 Tag 来区分镜像版本。

当然，镜像仓库除了可以存储用 DataFoundry 提供的构建功能输出的镜像外，也可以存储使用 Docker 构建的其他镜像，这些镜像以 Docker Pull 的方式存放在镜像仓库中。

Docker 镜像、镜像仓库和容器间的关系如下图所示：
![](registry.png)


## 服务部署（Deployments）

服务部署是指将一个或多个镜像部署到 DataFoundry 上，部署过程根据配置创建一个副本控制器（Replication Controller），副本控制器负责启动 Pod，并通过其中的定义来控制所启动的 Pod 的个数。

DataFoundry 上已部署的服务可以通过设置条件来触发自动部署，可触发自动部署的条件包括：部署配置变化、镜像变化。

## Pod

Pod 继承自 Kubernetes 的概念，是一个或多个容器部署在一起的集合。

可以定义 Pod 的计算资源。每一个 Pod 在 DataFoundry 集群中都会分配一个独立的 IP 地址，Pod 中的容器共享网络和本地存储。

Pod 的生命周期过程包括：通过配置进行定义，然后分配到一个集群节点上运行，在 Pod 所含容器运行结束后 Pod 也相应结束。
    
## 服务

服务是一组从 Docker 镜像运行的容器及路由组成的一个逻辑单元，作为对外提供服务的整体。包括：Pod、对外开放的服务端口、服务域名。服务可提供多副本部署、负载均衡等。

## 后端支持服务（Backing Services）

DataFoundry 作为大数据 PaaS 平台，以后端支持服务形式给平台使用者提供大数据服务组件，来提供给有状态服务使用。所谓后端支持服务是通过网络提供的云端服务组件，这些组件包含：

- 数据库组件：MySQL、GBase、MongoDB、PostgreSQL等；
- 消息组件：Kafka、RabbitMQ等；
- 计算组件：Storm、Spark等。

## 后端支持服务实例（Backing Service Instances）

当 DataFoundry 使用者需要使用后端支持服务时，需要首先申请后端支持服务实例。使用后端支持服务实例与服务绑定来获得后端支持服务的连接信息，使服务可以适配后端支持服务。

## 模板（Templates）