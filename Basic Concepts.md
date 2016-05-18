# 核心概念

DataFoundry是专注于大数据领域的PaaS云平台， 基于以Docker为代表的容器技术，为企业及开发者提供云端大数据应用构建、交付及运维的平台。提供应用生命周期全流程标准化的应用持续集成、镜像构建、持续交付、自动运维服务。

同时，DataFoundry整合了亚信大数据领域沉淀的大数据服务、应用、算法、解决方案等技术能力，同时引入第三方服务能力，可快速搭建并运维大数据平台、快速交付大数据应用。

DataFoundry打造以大数据应用为中心的云计算平台，优化开发运维环节，降低IT成本，提高了大数据应用和变现的效率，使得原本无法支撑的市场能够进入、使得原本无法成立的商业模式能够实现。市场机会在于建立一个大数据的PaaS公有云，并逐步将亚信现有本地实施转换为一套统一的私有云，从而打造应用生态。

本文提供给平台使用者在应用生命周期中的必要的核心概念。
    
## 容器（Containers）

linux容器技术提供轻量级的虚拟化设备，以便隔离进程、文件系统、网络等资源。

容器（Containers）是DataFoundry平台中定义的最小应用运行单元。

DataFoundry平台是基于Docker容器的，而Docker容器是基于Docker镜像（Images）运行的应用运行单元。
    
## 构建（Builds）

构建在DataFoundry系统中构建默认为Docker build。是指通过dockerfile、源代码为输入，构建出的可运行的镜像（images）为输出的过程。

在DataFoundry中支持代码源以git协议为基础的代码仓库，如Github、GitLab。
    
## 镜像（Images）
    
DataFoundry中镜像指Docker镜像，Docker镜像是Docker容器的基础。Docker镜像是通过dockerfile的定义将应用程序以及依赖打包到一个单独的虚拟容器中。这个容器可以运行在任何linux服务器上。这大大地提高了程序运行的灵活性和可移植性，无论需不需要许可、是在公共云还是私密云、是不是裸机环境等等。
    
## 镜像仓库（Image registry）
    
DataFoundry提供接收及存储Docker镜像的镜像仓库。镜像仓库存储了每次构建成功的镜像，以镜像TAG来区分每次构建的镜像版本。

当然，除了用DataFoundry提供的构建功能输出的镜像存储在镜像仓库中，镜像仓库也可以存储使用docker构建的其他镜像，将构建的镜像用docker pull的方式存放在镜像仓库中。

Docker镜像、镜像仓库、容器间关系如下图：
![](registry.png)
## Pods
Pod概念是继承Kubernetes的概念，Pod是一个或多个容器部署在一起的集合，可以给Pod定义计算资源。
每一个Pod在DataFoundry集群中都会分配一个独立的IP地址，在Pod中的容器共享网络和本地存储。
Pod的生命周期过程包括：通过配置进行定义，然后分配到一个集群节点上运行，在Pod所含容器运行结束后Pod也结束。

## Services

## 部署（Deployments）

    



## Routes
## Backing Services
## Backing Service Instances
## 模板（templates）





