import socket

host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
while True:
    conn , addr = s.accept()
    while True:
        data = conn.recv(1024)
        print "serv reply:"+data
conn.close()

