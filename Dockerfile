FROM registry.dataos.io/guestbook/gitbook
ADD . "/gitbook"
RUN cd /gitbook && gitbook init 
