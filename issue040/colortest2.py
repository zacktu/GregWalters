### colortest2.py

import curses
def main(stdscreen):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    stdscreen.clear()
    stdscreen.addstr(3,1," This is a test ",curses.color_pair(1))
    stdscreen.addstr(4,1," This is a test ",curses.color_pair(2))
    stdscreen.addstr(5,1," This is a test ",curses.color_pair(3))
    stdscreen.refresh()
    stdscreen.getch()
curses.wrapper(main)
