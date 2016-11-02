FROM resin/rpi-raspbian:jessie
RUN apt-get update && \
    apt-get -y install \
        build-essential \
        libzmq3-dev \
        python3 \
        python3-pip \
        python3-dev \
        --no-install-recommends && \
    pip3 install \
        pyzmq \
        RPi.GPIO
