FROM registry.dataos.io/library/tobegit-gitbook:latest
MAINTAINER tobe tobeg3oogle@gmail.com

RUN git clone https://github.com/DataFoundry/docs.git "/gitbook"
#RUN cd /gitbook/docs && mv * /github
RUN cd /gitbook && gitbook init 
