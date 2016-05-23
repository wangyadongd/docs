1 构建镜像

1.1 构建策略为docker的构建过程


以下以代码托管在github上举例说明。


1.1.1 代码仓库为公开


使用以下命令创建一个构建：


oc new-build https://github.com/asiainfoLDP/datahub_wordpress.git#master


运行结果如下：



	--> Found Docker image a913b48 (5 days old) from Docker Hub for "wordpress"
	
	    * An image stream will be created as "wordpress:latest" that will track the source image
	    * A Docker build using source code from https://github.com/asiainfoLDP/datahub_wordpress.git#master will be created
	      * The resulting image will be pushed to image stream "datahubwordpress:latest"
	      * Every time "wordpress:latest" changes a new build will be triggered
	
	--> Creating resources with label build=datahubwordpress ...
	    imagestream "wordpress" created
	    imagestream "datahubwordpress" created
	    buildconfig "datahubwordpress" created

	--> Success
	    Build configuration "datahubwordpress" created and build triggered.
	    Run 'oc logs -f bc/datahubwordpress' to stream the build progress.


	1.根据代码库中dockerfile中的from wordpress，将为wordpress:latest创建image stream，存放wordpress:latest镜像
	
	
	2.创建基于代码库https://github.com/asiainfoLDP/datahub_wordpress.git#master的构建
	
	
	3.创建用来存放构建完成后的镜像的imagestream:datahubwordpress
	
	
	4.当from的基础镜像发生改变时，将触发自动构建
	
	
	5.可以通过oc logs -f bc/datahubwordpress查看构建日志



查看构建的配置文件：

	oc export bc datahubwordpress

配置文件如下：

	apiVersion: v1
	kind: BuildConfig
	metadata:
	  annotations:
	    openshift.io/generated-by: OpenShiftNewBuild
	  creationTimestamp: null
	  labels:
	    build: datahubwordpress
	  name: datahubwordpress
	spec:
	  output:
	    to:
	      kind: ImageStreamTag
	      name: datahubwordpress:latest
	  postCommit: {}
	  resources: {}
	  source:
	    git:
	      ref: master
	      uri: https://github.com/asiainfoLDP/datahub_wordpress.git
	    secrets: []
	    type: Git
	  strategy:
	    dockerStrategy:
	      from:
	        kind: ImageStreamTag
	        name: wordpress:latest
	    type: Docker
	  triggers:
	  - github:
	      secret: wvnIqmIoLu_5HiMqQVsM
	    type: GitHub
	  - generic:
	      secret: mlEnK8yxlHUr9jdadyWJ
	    type: Generic
	  - type: ConfigChange
	  - imageChange: {}
	    type: ImageChange
	status:
	  lastVersion: 0



1.1.2 代码仓库为私有

第一步：创建secret，用来存储用户名和密码

	oc secrets new-basicauth secretname --username=github用户名 --password=github密码
	
	secretname为自己取的名字


第二步： 将secret加入serviceaccount/builder

	oc secrets add serviceaccount/builder secret/secretname

	由于构建过程默认使用serviceaccount/builder，所以只需将secret加入serviceaccount/builder即可

第三步： 


	oc new-build https://github.com/asiainfoLDP/datahub_wordpress.git#master --build-secret=secretname

查看构建的配置文件：

	apiVersion: v1
	kind: BuildConfig
	metadata:
	  annotations:
	    openshift.io/generated-by: OpenShiftNewBuild
	  creationTimestamp: null
	  labels:
	    build: datahubrepository
	  name: datahubrepository
	spec:
	  output:
	    to:
	      kind: ImageStreamTag
	      name: datahubrepository:latest
	  postCommit: {}
	  resources: {}
	  source:
	    git:
	      uri: https://github.com/asiainfoLDP/datahub_repository.git
	    secrets:
	    - destinationDir: .
	      secret:
	        name: secretname
	    type: Git
	  strategy:
	    dockerStrategy:
	      from:
	        kind: ImageStreamTag
	        name: golang:1.5.1
	    type: Docker
	  triggers:
	  - github:
	      secret: a7c_hhXMm7XTl_2OcGVC
	    type: GitHub
	  - generic:
	      secret: XJZ3c0g3rOh1Fzxkvumu
	    type: Generic
	  - type: ConfigChange
	  - imageChange: {}
	    type: ImageChange
	status:
	  lastVersion: 0


	可以看到git段中的secret部分添加了secret，new-build的时候还会提示输入用户名和密码，bc中的secret在start-build的构建过程中起作用，会带着认证信息去git clone私有仓库的代码


1.1.3 在构建中使用私有镜像仓库

当dockerfile中from的是私有镜像，或者构建镜像要推送到私有镜像仓库时，使用以下方法提供私有镜像仓库的认证信息。


第一步：创建secret


	oc secret new registry /root/.docker/config.json


第二步：添加secret到serviceaccount/builder


	oc secrets add serviceaccount/builder secrets/registry --for=pull


第三步：或者直接在bc中添加pull和push的secret：
	
	
	apiVersion: v1
	kind: BuildConfig
	metadata:
	  annotations:
	    openshift.io/generated-by: OpenShiftNewBuild
	  creationTimestamp: null
	  labels:
	    build: datahubwordpress
	  name: datahubwordpress
	spec:
	  output:
	    pushSecret:
	      name: registry
	    to:
	      kind: DockerImage
	      name: registry.dataos.io/harbor/test:test
	  postCommit: {}
	  resources: {}
	  source:
	    git:
	      uri: https://github.com/cherry4477/datahub_wordpress.git
	    secrets: []
	    type: Git
	  strategy:
	    dockerStrategy:
	      from:
	        kind: DockerImage
	        name: registry.dataos.io/harbor/harbor-ui:latest
	      pullSecret:
	        name: registry
	    type: Docker
	  triggers:
	  - github:
	      secret: spEagYnckgpU2_aQ0mKM
	    type: GitHub
	  - generic:
	      secret: 8vDO0nMFXfPOdRgT2I43
	    type: Generic
	  - type: ConfigChange
	status:
	  lastVersion: 0


2. 持续集成


有三种方式触发自动构建的持续集成：Webhook，Image change和Configuration change。三种方式可以同时使用。

一般在bc生成时，会自动加上trigger。webhook需要先去页面获取到，然后配到代码仓库的webhook中：

第一步：登录平台页面，点击浏览-builds,获取到githubwebhook

第二步：将webhook配置到github

配置完成后，当代码发生任何改变，都将触发自动构建。






	








