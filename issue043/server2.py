#!/usr/bin/env python
#server2.py

BUF_SIZE = 1024

import socket
soc = socket.socket()
hostname = socket.gethostname()
print('My hostname is ', hostname)
port = 21000
soc.bind((hostname,port))
soc.listen(5)
while True:
    con,address = soc.accept()
    data = con.recv(BUF_SIZE)
    if not data:
        break
    received = data.decode()
    con.send(received.encode())
    con.close()