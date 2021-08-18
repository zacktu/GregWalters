### colortest1.py

import curses
try:
    myscreen = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    myscreen.clear()
    myscreen.addstr(3,1," This is a test ",curses.color_pair(1))
    myscreen.addstr(4,1," This is a test ",curses.color_pair(2))
    myscreen.addstr(5,1," This is a test ",curses.color_pair(3))
    myscreen.refresh()
    myscreen.getch()
finally:
    curses.endwin()
