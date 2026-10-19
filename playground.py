import curses


def main(stdscr):
    # Hide the blinking cursor
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_BLUE)
    

    # Display some text
    stdscr.addstr(3,3," " * 40, curses.color_pair(1))
    for _ in range(4,20):
        stdscr.addstr(_,3," " * 2, curses.color_pair(1))
        stdscr.addstr(_,41," " * 2, curses.color_pair(1))
    stdscr.addstr(20 ,3," " * 40, curses.color_pair(1))

    stdscr.refresh()

    x = 5
    y = 5


    while True:

        stdscr.clear()

        # Display some text
        stdscr.addstr(3,3," " * 40, curses.color_pair(1))
        for _ in range(4,20):
            stdscr.addstr(_,3," " * 2, curses.color_pair(1))
            stdscr.addstr(_,41," " * 2, curses.color_pair(1))
        stdscr.addstr(20 ,3," " * 40, curses.color_pair(1))

        stdscr.addstr(y,x,"@", curses.color_pair(3))

        stdscr.addstr(0,0,f"y = {y},x = {x}")

        key = stdscr.getch()

                # Exit when Q is pressed
        if key in (ord("q"), ord("Q")):
            break

        # Move the character
        elif key == curses.KEY_UP:
            y = max(0, y - 1)
        elif key == curses.KEY_DOWN:
            y = min(curses.LINES - 1, y + 1)
        elif key == curses.KEY_LEFT:
            x = max(0, x - 1)
        elif key == curses.KEY_RIGHT:
            x = min(curses.COLS - 1, x + 1)

        stdscr.refresh()


# Initialize and safely clean up curses
curses.wrapper(main)

