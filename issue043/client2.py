
#!/usr/bin/env python
# client2.py

from socket import *
from time import time
from time import sleep
import sys
BUFSIZE = 4096

class CmdLine:
    def __init__(self,host):
        self.HOST = host
        self.PORT = 21000
        self.ADDR = (self.HOST, self.PORT)
        self.sock = None

    def makeConnection(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect(self.ADDR)

    def sendCmd(self, cmd):
        print("IN SENDCMD cmd = ", cmd)
        self.sock.send(cmd.encode())

    def getResults(self):
        data = self.sock.recv(BUFSIZE)
        print("RECEIVED DATA = ", data.decode())

if __name__ == '__main__':
    conn = CmdLine('puccini')
    conn.makeConnection()
    conn.sendCmd('ls -al')
    conn.getResults()
    conn.makeConnection()
    conn.sendCmd('BYE')
    conn.getResults()
