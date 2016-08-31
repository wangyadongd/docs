# Kettle

![](img/Kettle.png)

版本：v5.0.1

Kettle是一款国外开源的ETL工具。可以使用 job 作业方式或操作系统调度，来执行一个转换文件或作业文件，也可以通过集群的方式在多台机器上部署。

## Kettle后端服务

### 申请Kettle实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### Kettle仪表盘

无

### Kettle实例环境变量举例

- BSI_KETTLE_KETTLET2_USERNAME=-fz-_3-_328
- BSI_KETTLE_KETTLET2_PASSWORD=aa3*****d1a81a7fb9d3920b
- BSI_KETTLE_KETTLET2_HOST=sb-4fy****oi6rvc-kettle.service-brokers.svc.cluster.local
- BSI_KETTLE_KETTLET2_PORT="8080"
- BSI_KETTLE_KETTLET2_URI='File Uploader URL: http://sb-4******rvc-kettle-file-uploader.app.dataos.io'

- JSON:

{"Kettle":[{"name":"kettle-t2","label":"","plan":"standalone","credentials":{"Host":"sb-4**eoi6rvc-kettle.service-brokers.svc.cluster.local","Name":"","Password":"aa39**26d1a81a7fb9d3920b","Port":"8080","Uri":"File Uploader URL: http://sb-4fyd**8c-kettle-file-uploader.app.dataos.io","Username":"-fz-_3-_328","Vhost":""}}]}

### 使用Kettle实例

Kettle 实例与服务绑定后，使用host、 port、 username、 password、uri等环境变量连接 Kettle 实例。

## 其他文档

官方文档：http://community.pentaho.com/projects/data-integration/

开源社区：http://www.ukettle.org/

帮助文档：https://help.pentaho.com/Documentation/6.1

API文档：http://wiki.pentaho.com/display/EAI/Pentaho+Data+Integration+-+Java+API+Examples
