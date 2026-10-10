import curses
from input import input_data
from output import display_curses

def main():
    students, courses = input_data()
    if students:
        curses.wrapper(display_curses, students)

if __name__ == "__main__":
    main()