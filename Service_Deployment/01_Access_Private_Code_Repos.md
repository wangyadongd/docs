##  第一节 访问私有代码仓库

为了让 DataFoundry 在构建镜像时访问私有代码，我们需要在 DataFoundry 中创建 secrets 资源，并把 secrets 绑定到平台中。具体过程如下：
  
### 创建访问私有代码库 secrets

``` 
oc secrets new-basicauth <basicsecret> \
--username=<USERNAME> \
--password=<PASSWORD>
``` 
其中：

- `basicsecret` 是给 secrets 起的一个可以识别的名字  
- `USERNAME` 是登陆代码库的用户名  
- `PASSWORD` 是登陆代码库的用户密码  

### 绑定 secrets 到平台默认的镜像构建账户中

``` 
oc secrets add serviceaccount/builder secrets/<basicsecret>
``` 

### 在 buildconfig 中指定 secrets

``` 
apiVersion: "v1"
kind: "BuildConfig"
metadata:
  name: "sample-build"
spec:
  output:
    to:
      kind: "ImageStreamTag"
      name: "sample-image:latest"
  source:
    git:
      uri: "https://github.com/user/app.git" 
    sourceSecret:
      name: "<basicsecret>"
    type: "Git"
  strategy:
    sourceStrategy:
      from:
        kind: "ImageStreamTag"
        name: "python-33-centos7:latest"
    type: "Source"
```   