#!/usr/bin/env python
#-------------------------------
# Curses Programming Template
#-------------------------------

import curses

def InitScreen(Border):
    if Border == 1:
        myscreen.border(0)

#==========================================================
#   MAIN LOOP
#==========================================================
myscreen = curses.initscr()
InitScreen(1)
try:
    myscreen.refresh()
    ############ Your Code Stuff Here...
    print('My code is here')
    ############
    myscreen.addstr(1,1, "Press Any Key to Continue")
    myscreen.getch()
finally:
    curses.endwin()