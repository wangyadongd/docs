##  第四节 让服务支持 https 协议访问  

https 服务现在已经非常普及了，在 DataFoundry 上也可以支持。具体使用上可分两种情况，服务本身已使用 https 和服务本身未使用 https。
   
###  服务本身已使用 https 协议  

如果服务本身已使用 https 方式部署，让 DataFoundry 支持 https 访问协议就非常简单了，只需通过如下命令创建 https 协议的 route 即可：
  
```
 oc create route passthrough [NAME] \
 --service=SERVICE \
 --hostname=[HOSTNAME]
``` 

其中：  
- `NAME` 参数是 route 的名字；
- `SERVICE` 参数是 route 所对应的 service 名称，这是为了通过 service 获取需通过 route 分发流量的 POD IP 和端口信息；
- `HOSTNAME` 参数是 route 对外提供的域名信息。    
  
###  服务本身未使用 https 协议  

这种情况可以需要先为服务申请签名证书，然后再通过如下命令创建使用 https 协议的 route：

```
oc create route edge [NAME] \
--service=SERVICE \
--hostname=[HOSTNAME] \
--key==example-test.key \
--cert=example-test.crt
```   

其中：  
- `NAME`、`SERVICE`、`HOSTNAME` 的含义之前已经介绍过；
- `key`、`cert` 参数是从签名机构申请回来的证书文件目录。