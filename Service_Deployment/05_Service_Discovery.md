## 第五节 通过 service 完成服务发现  

kubernetes 的 service 功能除了可以在平台内部进行负载均衡外，还可以完成在平台内的服务发现。

service 名称是平台内的 DNS 短地址，因此可以通过 service 名称进行同一命名空间内服务间的相互发现和访问，跨命名空间的service访问地址为 `<servicename>.<namespace>.svc.cluster.local`。