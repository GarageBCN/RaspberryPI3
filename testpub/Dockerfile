FROM hypriot/rpi-python
ADD testpub.py /
RUN apt-get update && \
    apt-get -y install build-essential && \
    pip install pyzmq
ENTRYPOINT python /testpub.py
