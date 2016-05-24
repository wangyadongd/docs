# 第五章 镜像仓库

# 登录仓库

浏览器中输入registry.dataos.io,登录registry.dataos.io到镜像页面。

登录镜像仓库界面：由于镜像仓库与LDAP对接，所以登录镜像仓库需要输入LDAP的用户名和密码。

命令行登录镜像仓库：

    sudo docker login registry.dataos.io
    username输入ldap用户名
    password输入ldap用户名的密码
    email随便输入，没有限制
    login successfully！

# 用户私有镜像仓库的操作

镜像仓库通过项目管理镜像。用户对于项目有三种权限：admin,developer和guest。其中admin可以对项目做增加删除项目用户和控制用户权限，是否公开项目以及pull和push镜像的操作；developer可以进行pull和push镜像的操作；guest只有pull镜像的权限。


各项目登陆后，首先创建自己的项目，选择是否公开，然后加入项目成员，并授权角色。之后各成员可以pull或者push该项目下的镜像。如果是私有项目，做pull或者push镜像操作的时候需要使用以上命令行方式先登录。如果项目设置为公开，则可以不登录。

# 公共镜像仓库的操作

项目设置为公开时，其他所有用户都可以对项目中的镜像进行pull操作，但是不可以进行push操作。默认公开项目为library，与docker hub的library项目类似。所有用户都可以对library项目中的镜像进行pull操作，但是不可以push。其他用户公开的项目也可以在公开项目中看到，同样也可以进行pull操作，但是不可以进行push操作。

