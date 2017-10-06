import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',8080))

for n in range(1,11):
    time.sleep(1)
    sock.send(str(n))
sock.close()
