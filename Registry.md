# 第五章 镜像仓库

## 登录仓库

在浏览器中输入 registry.dataos.io 登录镜像仓库页面。

由于镜像仓库与 LDAP 对接，所以登录镜像仓库需要输入 LDAP 的用户名和密码。

命令行登录镜像仓库：

    sudo docker login registry.dataos.io
    username 输入 LDAP 用户名
    password 输入 LDAP 用户名的密码
    email 任意输入，没有限制
    login successfully!

## 用户私有镜像仓库的操作

镜像仓库通过项目管理镜像。

用户对于项目有三种权限：admin，developer 和 guest。其中
- admin 可以进行增加、删除项目用户，控制用户权限，是否公开项目和 pull 和 push 镜像的操作；
- developer 可以进行 pull 和 push 镜像的操作；
- guest 只有 pull 镜像的权限。

用户登陆后，首先创建自己的项目，选择是否公开，然后加入项目成员，并授权角色。之后各成员可以 pull 或者 push 该项目下的镜像。

如果是私有项目，做 pull 或者 push 镜像操作时，需要先使用上述命令行方式登录。如果项目设置为公开，则可以不登录。

## 公共镜像仓库的操作

项目设置为公开时，所有用户都可以对项目中的镜像进行 pull 操作，但不可以进行 push 操作。

默认公开项目为 library，与 docker hub 的 library 项目类似。其他用户公开的项目也可以在公开项目中看到。