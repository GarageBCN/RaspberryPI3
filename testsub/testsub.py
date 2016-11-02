import sys
import zmq

if len(sys.argv) < 3:
    print("You need at least two arguments: publisher address and output file")
address = sys.argv[1]
output_file = sys.argv[2]

ctx = zmq.Context()
socket = ctx.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, "")
socket.connect(address)
msg=""

with open(output_file, "w+") as f:
    while msg != "quit":
        if msg != "":
            print(msg, file=f, flush=True)
        msg = socket.recv_pyobj()
