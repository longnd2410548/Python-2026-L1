import curses
from input import input_data, compress_data
from output import display_curses
import os

def main():
    students, courses = input_data()
    if students:
        curses.wrapper(display_curses, students)
    
    if os.path.exists("students.txt"):
        compress_data()

if __name__ == "__main__":
    main()