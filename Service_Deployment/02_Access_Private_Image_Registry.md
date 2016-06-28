##  第二节 访问私有镜像库

有时我们需要部署已经上传到私有镜像仓库里的容器镜像，这时也需要在 DataFoundry 配置相关 secrets来保证 DataFoundry 对私有镜像仓库有足够的访问权限。具体过程如下：

### 创建访问私有镜像库 secrets

``` 
oc secrets new-dockercfg <dockerpullsecret> \
--docker-server=<registry_server> \
--docker-username=<USERNAME> \ 
--docker-password=<PASSWORD> \
--docker-email=<EMAIL>
``` 

其中：
- `dockerpullsecret` 是给 secrets 起的一个可以识别的名字；
- `registry_server` 是需要 DataFoundry 登陆的私有镜像仓库地址，例如 registry.dataos.io；
- `USERNAME` 是登陆镜像库的用户名；
- `PASSWORD` 是登陆镜像库的用户密码；
- `EMAIL` 是登陆镜像库的 email 地址。

### 绑定 secrets 到平台默认的镜像部署系统账户中

```
oc secrets add serviceaccount/<default> secrets/<dockerpullsecret>
```

其中：
- `default` 是 DataFoundry 默认的镜像部署系统账户，用户也可以指定需要的系统账户。