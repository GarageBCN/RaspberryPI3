import os
import sys
import zmq

if len(sys.argv) < 3:
    print("You need at least two arguments: binding address and file to read")
    sys.exit(1)
address = sys.argv[1]
data_file = sys.argv[2]

ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)
socket.bind(address)

os.mkfifo(data_file, mode=0o666)
with open(data_file) as f:
    stream=""
    while stream != "quit":
        stream=f.readline()
        if stream != "":
            socket.send_pyobj(stream)
os.unlink(data_file)
