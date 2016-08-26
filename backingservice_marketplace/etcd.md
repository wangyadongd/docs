# etcd


![](img/ETCD.png)

版本：v2.3.0

etcd是一个高可用的键值存储系统,主要用于共享配置和服务发现。通过Raft一致性算法处理日志复制以保证强一致性。

## etcd后端服务

### 申请etcd实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### etcd仪表盘

无

### etcd实例的环境变量举例

- BSI_ETCD_ETCDTEST_NAME= 
- BSI_ETCD_ETCDTEST_USERNAME=etcduser
- BSI_ETCD_ETCDTEST_PASSWORD=0b48862d05e57aa892c3b1b97cb2b88d
- BSI_ETCD_ETCDTEST_HOST=sb-6z5t2hupy5rtc-etcd.app.dataos.io
- BSI_ETCD_ETCDTEST_PORT="80"
- BSI_ETCD_ETCDTEST_VHOST
- BSI_ETCD_ETCDTEST_URI=http://sb-6z5t2hupy5rtc-etcd.app.dataos.io:80
- JSON:

{"ETCD":[{"name":"etcd-test","label":"","plan":"standalone","credentials":{"Host":"sb-6z5t2hupy5rtc-etcd.app.dataos.io","Name":"","Password":"0b48862d05e57aa892c3b1b97cb2b88d","Port":"80","Uri":"http://sb-6z5t2hupy5rtc-etcd.app.dataos.io:80","Username":"etcduser","Vhost":""}}]}



## 其他文档

官方文档：https://coreos.com/etcd/

帮助文档：https://coreos.com/etcd/docs/2.3.0/index.html

API文档：https://coreos.com/etcd/docs/0.4.7/etcd-api/


