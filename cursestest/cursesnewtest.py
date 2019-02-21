from unicurses import *

def main():
    stdscr = initscr()
    a = getch()
    b = getch()
    addstr(a+b-96)
    c = getch()

    endwin()
    return c

if (__name__ == "__main__"):
    print(main())
