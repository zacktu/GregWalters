#!/usr/bin/env python
#server2.py

BUF_SIZE = 1024

import os
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
    command = data.decode()
    outfile = os.popen(command)
    chrfile = outfile.read()
    con.send(chrfile.encode())
    con.close()