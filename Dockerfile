FROM hypriot/rpi-python
ADD python/testled.py /
RUN apt-get update && \
    apt-get -y install build-essential && \
    pip install RPi.GPIO
ENTRYPOINT python /testled.py
