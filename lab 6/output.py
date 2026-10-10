import curses

def display_curses(stdscr, students):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== Student ranking by GPA ===")

    for row, s in enumerate(students, start=2):
        stdscr.addstr(row, 0, f"{s.get_id()} - {s.get_name()}: GPA = {s.get_gpa():.2f}")

    stdscr.addstr(len(students) + 3, 0, "Press any key to exit!")
    stdscr.refresh()
    stdscr.getch()