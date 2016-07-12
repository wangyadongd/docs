FROM registry.dataos.io/guestbook/gitbook
ADD . "/gitbook"
WORKDIR /gitbook
RUN cd /gitbook && gitbook init
CMD ["gitbook", "serve"]
