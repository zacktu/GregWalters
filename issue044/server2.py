#!/usr/bin/env python
# server2.py

from socket import *
import sys
import os

BUFSIZ = 4096
HOST = ''
PORT = 29876
ADDR = (HOST,PORT)

class ServCmd:
    def __init__(self):
       self.serv = socket( AF_INET,SOCK_STREAM)
       self.serv.bind((ADDR))
       self.cli = None
       self.listeningloop  = 0
       self.processingloop = 0
       self.player = 1
       self.gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]
       self.run()

    def run(self):
        self.listeningloop = 1
        while self.listeningloop:
            self.listen()
            self.processingloop = 1
            while self.processingloop:
               self.procCmd()
            self.cli.close()
        self.serv.close()

    def listen(self):
        self.serv.listen(5)
        print('Listening for Client')
        cli,addr = self.serv.accept()
        self.cli = cli
        print('Connected to ', addr)

    def procCmd(self):
        cmd = self.cli.recv(BUFSIZ)
        if not cmd: return
        print("Received command: ", cmd)
        self.servCmd(cmd)
        if self.processingloop: 
                if cmd == 'Start':
                    self.InitGameBoard()
                    self.PrintGameBoard(1)
                if cmd[:4] == 'Move':
                    print("MOVE COMMAND")
                    position = cmd[5:]
                    print("Position = " + position)
                    if position[0] == 'A':
                        row = 0
                    elif position[0] == 'B':
                        row = 1                       
                    elif position[0] == 'C':
                        row = 2
                    else:
                        self.cli.send('Invalid position')
                        return
                    col = int(position[1])-1
                    print("Col = %s,Row = %s" % (col,row))
                    if row < 0 or row > 2:
                        self.cli.send('Invalid position')
                        return
                    if self.gameboard[row][col] == '-':
                        if self.player == 1:
                            self.gameboard[row][col] = "X"
                        else:
                            self.gameboard[row][col] = "O"
                    self.PrintGameBoard(0)
            
    def servCmd(self,cmd):
        cmd = cmd.strip()
        if cmd == 'GOODBYE': 
           self.processingloop = 0
        
    def InitGameBoard(self):
        self.gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]

    def PrintGameBoard(self,firsttime):
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
        if firsttime == 0:
            if self.player == 1:
                ret = self.checkwin("X")
            else:
                ret = self.checkwin("O")
            if ret == True:
                if self.player == 1:
                    outp += "Player 1 WINS!" 
                else:
                    outp += "Player 2 WINS!"
            else:
                if self.player == 1:
                    self.player = 2
                else:
                    self.player = 1
                outp += ('Enter move for player %s' % self.player)
        self.cli.send(outp)
        
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
            elif self.gameboard[0][2] == player and self.gameboard[1][1] == player and \
                    self.gameboard[2][0] == player:
              print("*********\n\n%s wins\n\n*********" % player)
              playerwin = True
              return playerwin
        else:
            playerwin = False
            return playerwin
        
if __name__ == '__main__':
   serv = ServCmd()
