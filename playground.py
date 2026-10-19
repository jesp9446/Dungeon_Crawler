import curses


def main(stdscr):
    # Hide the blinking cursor
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_BLACK)

    # Display some text
    stdscr.addstr(3,3," " * 40, curses.color_pair(1))
    for _ in range(4,20):
        stdscr.addstr(_,3," " * 2, curses.color_pair(1))
        stdscr.addstr(_,41," " * 2, curses.color_pair(1))
    stdscr.addstr(20 ,3," " * 40, curses.color_pair(1))

    stdscr.refresh()

    stdscr.getch()

# Initialize and safely clean up curses
curses.wrapper(main)

