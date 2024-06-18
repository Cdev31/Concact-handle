from src.interfaces.menu import menu
import curses



def loop( stdscr ):
    curses.curs_set(0)
    menu()
    curses.curs_set(1)

if __name__ == '__main__':
    curses.wrapper(loop)
        