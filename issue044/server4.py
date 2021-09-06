#!/usr/bin/env python
#GregWalters/issue044
# server4.py

from socket import *
import sys
import os

BUFSIZ = 4096
HOST = ''
PORT = 29877
ADDR = (HOST,PORT)

class ServCmd:
    def __init__(self):
       self.serv = socket( AF_INET,SOCK_STREAM)
       self.serv.bind((ADDR))
       self.cli = None
       self.listeningloop  = False
       self.processingloop = False
       self.player = 1
       self.gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]
       self.run()

    def run(self):
        print("ENTERING run")
        self.listeningloop = True
        while self.listeningloop:
            print("INSIDE while self.listeningloop")
            self.listen()
            self.processingloop = True
            while self.processingloop:
                print("INSIDE while self.processingloop")
                self.procCmd()
            self.cli.close()
            print("WILL CLOSE self.serv")
        self.serv.close()
        print('SERVER IS CLOSED')
        print("SERVER IS CLOSED")

    def listen(self):
        self.serv.listen(5)
        print('Listening for Client')
        cli,addr = self.serv.accept()
        self.cli = cli
        print('Connected to ', addr)

    def procCmd(self):
        print("ENTERING procCmd")
        cmd = self.cli.recv(BUFSIZ).decode()
        print("In procCmd cmd = %s" % cmd)
        if not cmd:
            print("CMD NOT AVAILABLE WILL RETURN")
            return
        print("Received command: ", cmd)
        self.servCmd(cmd)
        if self.processingloop:
            if cmd == 'Start':
                print("Command was Start")
                self.InitGameBoard()
                print("SHOULD HAVE INITIALIZED BOARD")
                self.PrintGameBoard(True)
                print("SHOULD HAVE PRINTED BOARD")
            if cmd[:4] == 'Move':
                print("COMMAND WAS MOVE")
                position = cmd[5:]
                print("Position = " + position)
                if position[0] == 'A':
                    row = 0
                elif position[0] == 'B':
                    row = 1
                elif position[0] == 'C':
                    row = 2
                else:
                    errormessage = "Error: Row " + position[0] + " is an invalid position."
                    errormessage = "Error: Row %s is an invalid position." % position[0]
                    self.cli.send(errormessage.encode())
                    return
                print("ROW = ", row)
                col = int(position[1])-1
                print("COL = ", col)
                print("Col = %s,Row = %s" % (col,row))
                if col < 0 or col > 2:
                    errormessage = "Error: Column %s is an invalid position." % position[1]
                    self.cli.send(errormessage.encode())
                    return
                if self.gameboard[row][col] == '-':
                    if self.player == 1:
                        self.gameboard[row][col] = "X"
                    else:
                        self.gameboard[row][col] = "O"
                self.PrintGameBoard(False)
                print("Bottom of Move should have printed board")
                #print("That's all Folks!")
                #sys.exit()

    def servCmd(self,cmd):
        cmd = cmd.strip()
        if cmd == 'GOODBYE':
            print("RECEIVED GOODBYE COMMAND WILL MAKE LISTENING and PROCESSING LOOPS FALSE")
            self.listeningloop = False
            self.processingloop = False

        
    def InitGameBoard(self):
        self.gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]

    def PrintGameBoard(self, firsttime):
        #Print the header row
        outp = ('   1   2   3') + chr(13) + chr(10)
        outp += (" A {0} | {1} | {2}" \
                .format(self.gameboard[0][0],self.gameboard[0][1], \
                        self.gameboard[0][2])) \
                + chr(13)+chr(10)
        outp += ('  ------------')+ chr(13)+chr(10)
        outp += (" B {0} | {1} | {2}" \
                .format(self.gameboard[1][0],self.gameboard[1][1], \
                        self.gameboard[1][2])) \
                + chr(13)+chr(10)
        outp += ('  ------------')+ chr(13)+chr(10)
        outp += (" C {0} | {1} | {2}" \
                .format(self.gameboard[2][0],self.gameboard[2][1], \
                        self.gameboard[2][2])) \
                + chr(13)+chr(10)
        outp += ('  ------------')+ chr(13)+chr(10)
        if firsttime:
            outp += ('\nEnter move for player 1')
        else:
            if self.player == 1:
                ret = self.checkwin("X")
            else:
                ret = self.checkwin("O")
            if ret == True:
                if self.player == 1:
                    outp += "\nPlayer 1 WINS!\n"
                else:
                    outp += "\nPlayer 2 WINS!\n"
            else:
                if self.player == 1:
                    self.player = 2
                else:
                    self.player = 1
            outp += ('\nEnter move for player %s' % self.player)
        print("THE BOARD:")
        print(outp)
        self.cli.send(outp.encode())
        
    def checkwin(self,player):
        #loop through rows and columns
        for c in range(0,3):
        #check for horizontal line
            if self.gameboard[c][0] == player \
                    and self.gameboard[c][1] == player \
                    and self.gameboard[c][2] == player:
              print("*********\n\n%s wins\n\n*********" % player)
              playerwin = True
              return playerwin
            #check for vertical line
            elif self.gameboard[0][c] == player \
                    and self.gameboard[1][c] == player \
                    and self.gameboard[2][c] == player:
              print("*********\n\n%s wins\n\n*********" % player)
              playerwin = True
              return playerwin
            #check for diagonal win (left to right)
            elif self.gameboard[0][0] == player \
                    and self.gameboard[1][1] == player \
                    and self.gameboard[2][2] == player:
              print("*********\n\n%s wins\n\n*********" % player)
              playerwin = True
              return playerwin
            #check for diagonal win (right to left)
            elif self.gameboard[0][2] == player \
                    and self.gameboard[1][1] == player \
                    and self.gameboard[2][0] == player:
              print("*********\n\n%s wins\n\n*********" % player)
              playerwin = True
              return playerwin
        else:
            playerwin = False
            return playerwin

if __name__ == '__main__':
   serv = ServCmd()


