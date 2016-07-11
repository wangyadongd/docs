FROM registry.dataos.io/library/tobegit-gitbook:latest
MAINTAINER tobe tobeg3oogle@gmail.com
ENV VERSION=3.1.1
ADD . "/gitbook"
#RUN echo "registry=https://registry.npm.taobao.org" > ~/.npmrc
#RUN cd /gitbook/docs && mv * /github
RUN npm install --global gitbook-cli && gitbook fetch ${VERSION}  
RUN cd /gitbook && gitbook install && gitbook init 
