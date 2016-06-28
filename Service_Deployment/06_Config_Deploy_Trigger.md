##  第六节 配置自动部署触发器

很多时候，我们希望在镜像构建完成以后可以自动完成镜像的部署，这时可以使用 DataFoundry 提供的基于镜像变化的自动化部署触发机制，具体使用方法如下：

```
oc set triggers dc/<deploymentconfig_name>  --from-image=<image_name> --container=<container_name>
```

其中：  
- `deploymentconfig_name` 是需要在镜像变化是由平台触发的部署配置名；
- `image_name` 是被平台跟踪的镜像仓库地址，如果镜像库发生变化就会触发部署；   
- `container_name` 对应 POD 中的应容器名，在触发部署时平台会用上面的容器镜像来更新 POD 中的容器。

通过 `oc set triggers dc/<deploymentconfig_name>`  命令可以查看已经配置在平台中的触发器；  
通过 `oc set triggers dc/<deploymentconfig_name> --from-image --remove` 命令可以删除已经配置的镜像触发器。