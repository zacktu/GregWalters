#!/usr/bin/env python
#server1.py

import socket
soc = socket.socket()
hostname = socket.gethostname()
print('My hostname is ', hostname)
port = 21000
soc.bind((hostname,port))
soc.listen(5)
while True:
    con,address = soc.accept()
    print("I'm now connected to ",address)
    tosend = "Hello and Goodbye"
    encoded = tosend.encode()
    con.send(encoded)
    con.close()
