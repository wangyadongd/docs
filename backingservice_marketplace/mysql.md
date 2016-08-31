# Mysql

![](img/Mysql.png)

版本：

MySQL是WEB应用方面最好的关系数据库管理系统应用软件之一。具有体积小、速度快、总体拥有成本低的特性。

## Mysql后端服务

### 申请Mysql实例

查看后端服务、申请后端服务实例、绑定后端服务实例参见功能介绍《第四节 后端支持服务》章节。

### Mysql仪表盘

由于目前Dashboard到mysql的验证方式设置为Basic auth，并没有采用sso单点登录，而不同浏览器对此的安全设置不一样。所以暂时无法通过Safari来访问，只能通过Chrome和Firefox不通过代理访问（通过代理不支持Basci auth）。

### Mysql实例环境变量举例

- BSI_MYSQL_MYSQLTEST_URI=mysql://b22a39570dbd4b2:27f2acb7a57df94@mysqlnocase.servicebroker.dataos.io:3306/f097a5769f99f13
- BSI_MYSQL_MYSQLTEST_NAME=f097a5769f99f13
- BSI_MYSQL_MYSQLTEST_USERNAME=b22a39570dbd4b2
- BSI_MYSQL_MYSQLTEST_PASSWORD=27f2acb7a57df94
- BSI_MYSQL_MYSQLTEST_HOST=mysqlnocase.servicebroker.dataos.io
- BSI_MYSQL_MYSQLTEST_PORT="3306"

- JSON:

{"Mysql":[{"name":"mysql-test","label":"","plan":"NoCase","credentials":{"Host":"mysqlnocase.servicebroker.dataos.io","Name":"f097a5769f99f13","Password":"27f2acb7a57df94","Port":"3306","Uri":"mysql://b22a39570dbd4b2:27f2acb7a57df94@mysqlnocase.servicebroker.dataos.io:3306/f097a5769f99f13","Username":"b22a39570dbd4b2","Vhost":""}}]}

### 使用Mysql实例

Mysql 实例与服务绑定后，使用host、 port、 username、 password、uri、name等环境变量连接 Kettle 实例。

## 其他文档

官网网址：https://www.mysql.com/

帮助文档：http://dev.mysql.com/doc/relnotes/mysql/5.6/en/news-5-6-27.html

API文档：http://dev.mysql.com/doc/ndbapi/en/preface.html
