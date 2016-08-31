# NiFi

![](img/nifiDrop.png)

版本：v0.6.1

NiFi 是一个易于使用、功能强大而且可靠的数据处理和分发系统。支持高度可配置的指示图的数据路由、转换和系统中介逻辑。

## NiFi后端服务

### 申请NiFi实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### NiFi仪表盘

无

### NiFi实例环境变量举例

- BSI_NIFI_NIFITEST_HOST=sb-fgkeujisbgcee-nifi.service-brokers.svc.cluster.local
- BSI_NIFI_NIFITEST_PORT="8080"

- JSON:

{"NiFi":[{"name":"NiFi-test","label":"","plan":"standalone","credentials":{"Host":"sb-fgkeujisbgcee-nifi.service-brokers.svc.cluster.local","Name":"","Password":"","Port":"8080","Uri":"","Username":"","Vhost":""}}]}

### 使用NiFi实例

NiFi 实例与服务绑定后，使用host、 port等环境变量连接 NiFi 实例。

## 其他文档

官网网址：http://nifi.apache.org/

帮助文档：http://nifi.apache.org/docs.html

API文档：http://nifi.apache.org/docs.html
