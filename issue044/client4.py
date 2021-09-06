
#!/usr/bin/env python
#GregWalters/issue044
# client4.py

from socket import *
from time import time
from time import sleep
import sys
BUFSIZE = 4096

class CmdLine:
    def __init__(self,host):
        self.HOST = host
        self.PORT = 29877
        self.ADDR = (self.HOST,self.PORT)
        self.sock = None

    def makeConnection(self):
        self.sock = socket( AF_INET,SOCK_STREAM)
        self.sock.connect(self.ADDR)

    def sendCmd(self, cmd):
        print(cmd)
        self.sock.send(cmd.encode())

    def getResults(self):
        data = self.sock.recv(BUFSIZE)
        print(data.decode())

class procActions:
    def checkAction(self, action):
        print('Entering checkAction with action = %s ' % action)
        if action == 'GOODBYE':
            print('checkAction will return %s ' % action)
            return action
        elif len(action) == 2 \
                and action[0] in 'ABC' \
                and action[1] in '123':
            print('checkAction will return %s ' % action)
            return 'Move ' + action
        else:
            print('checkAction will return %s ' % action)
            return 'Invalid'

if __name__ == '__main__':
    conn = CmdLine('localhost')
    conn.makeConnection()
    conn.sendCmd('Start')
    conn.getResults()
    processActions = procActions()

    while True:
        action = input()
        print("ACTION IS %s" % action)
        checkedAction = processActions.checkAction(action)
        print ('checkAction has returned %s ' % action)
        if checkedAction == 'GOODBYE':
            conn.sendCmd(action)
            break
        elif checkedAction == 'Invalid':
            print('\r%s is not a valid action.  Enter another.' % action)
        else:
            conn.sendCmd(checkedAction)
            conn.getResults()

    print("That's all folks!")
    #sys.exit()

    '''
    
    conn.sendCmd('Move A1')
    conn.getResults()
    conn.sendCmd('Move B2')
    conn.getResults()
    conn.sendCmd('Move C2')
    conn.getResults()
    conn.sendCmd('Move B3')
    #conn.sendCmd('Move A1')
    conn.getResults()
    conn.sendCmd('Move B5')
    conn.getResults()
    conn.sendCmd('Move C1')
    conn.getResults()
    conn.sendCmd('Move A3')
    conn.getResults()
    conn.sendCmd('Move C3')
    conn.getResults()
    conn.sendCmd('GOODBYE')
    '''
