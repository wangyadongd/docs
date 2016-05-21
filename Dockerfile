FROM registry.dataos.io/library/tobegit-gitbook:latest
MAINTAINER tobe tobeg3oogle@gmail.com

ADD . "/gitbook"
#RUN cd /gitbook/docs && mv * /github
RUN cd /gitbook && gitbook init 
