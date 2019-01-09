FROM ubuntu:16.04
LABEL maintainer="bugra@ymail.com"
RUN apt-get update && apt-get install -y \
        curl \
        gnupg

RUN echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1
RUN curl -s https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -
RUN apt-get update && apt-get install -y \
        tensorflow-model-server

RUN  apt-get clean && \
        rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/models /app/tf_serving_scripts
COPY models/fashion_mnist/ /app/models
COPY fashion_mnist.sh /app/tf_serving_scripts

# GRPC Port
EXPOSE 8500
# HTTP REST API Port
EXPOSE 8501  

ENTRYPOINT ["/bin/sh", "/app/tf_serving_scripts/fashion_mnist.sh"]
