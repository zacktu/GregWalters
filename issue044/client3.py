
#!/usr/bin/env python
#GregWalters/issue044
# client3.py

from socket import *
from time import time
from time import sleep
import sys
BUFSIZE = 4096

class CmdLine:
    def __init__(self,host):
        self.HOST = host
        self.PORT = 29876
        self.ADDR = (self.HOST,self.PORT)
        self.sock = None

    def makeConnection(self):
        self.sock = socket( AF_INET,SOCK_STREAM)
        self.sock.connect(self.ADDR)

    def sendCmd(self, cmd):
        print("SENT CMD = ", cmd)
        self.sock.send(cmd.encode())

    def getResults(self):
        data = self.sock.recv(BUFSIZE)
        print("RECEIVED DATA = :")
        print(data.decode())

if __name__ == '__main__':
    conn = CmdLine('localhost')
    conn.makeConnection()
    conn.sendCmd('Start')
    conn.getResults()
    conn.sendCmd('Move A1')
    conn.getResults()
    conn.sendCmd('Move B2')
    conn.getResults()
    conn.sendCmd('Move C2')
    conn.getResults()
    conn.sendCmd('Move B3')
    conn.sendCmd('GOODBYE')
