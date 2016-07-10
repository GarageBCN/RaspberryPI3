FROM hypriot/rpi-python
ADD testsub.py /
RUN apt-get update && \
    apt-get -y install build-essential && \
    pip install pyzmq
ENTRYPOINT python /testsub.py
