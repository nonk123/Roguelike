#!/usr/bin/python3

import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Hello, World!")
    stdscr.addstr(1, 0, "Press any key to exit.\n")
    stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(main)
