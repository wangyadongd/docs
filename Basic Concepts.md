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
    
## 镜像（Images）
    
    DataFoundry中镜像指Docker镜像，Docker镜像是Docker容器的基础。Docker镜像是将应用程序以及应用程序的依赖打包到一个单独的虚拟容器中。这个容器可以运行在任何linux系统中，
## 镜像仓库（Image registry）
## 部署（Deployments）

## Pods
## Services
## Routes
## Backing Services
## Backing Service Instances
## 模板（templates）





