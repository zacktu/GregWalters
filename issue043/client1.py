#!/usr/bin/python
# client1.py
#====================

import socket
soc = socket.socket()
hostname = socket.gethostname()
print("hostname = ", hostname)
port = 21000
soc.connect((hostname, port))

#print(soc.recv(1024))
print(soc.recv(1024).decode())
soc.close