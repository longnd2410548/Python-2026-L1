import math
import curses
import numpy as np

class Student:
    def __init__(self, s_id, name, dob):
        self.__id = s_id
        self.__name = name
        self.__dob = dob 
        self.__marks = {}
        self.__gpa = 0.0

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def get_marks(self):
        return self.__marks
    def get_gpa(self):
        return self.__gpa
    
    def set_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def caculate_gpa(self, course):
        marks_list = []
        credits_list = []
        for c in course:
            c_id = c.get_id()
            if c_id in self.__marks:
                marks_list.append(self.__marks[c_id])
                credits_list.append(c.get_credits())
        
        if not credits_list:
            self.__gpa = 0.0
            return self.__gpa

        np_marks = np.array(marks_list, dtype=float)
        np_credits = np.array(credits_list, dtype=float)

        total_credits = np.sum(np_credits)
        if total_credits == 0:
            self.__gpa = 0.0
        else:
            self.__gpa = np.sum(np_marks * np_credits) / total_credits
            
        return self.__gpa

class Course:
    def __init__(self, c_id, name, credits):
        self.__id = c_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits

def round_down(score):
    return math.floor(score * 10) / 10.0
    
def input_data():
    students = []
    courses = []
    num_s = int(input("Input number of students: "))
    for i in range(num_s):
        print(f"Input for student {i+1}: ")
        s_id = input("Student ID: ").strip()
        name = input("Student name: ").strip()
        dob = input("Student DoB: ").strip()
        students.append(Student(s_id, name, dob))

    num_c = int(input("Enter number of courses: "))
    for i in range(num_c):
        print(f"Enter for course {i+1}: ")
        c_id = input("Course ID: ").strip()
        name = input("Course name: ").strip()
        credits = int(input("Credits: "))
        courses.append(Course(c_id, name, credits))

    print("\nEnter Marks: ")
    for c in courses: 
        print(f"\n--- Course: {c.get_name()} ---")
        for s in students:
            mark = float(input(f"Mark for student {s.get_name()}: "))
            mark = round_down(mark)
            s.set_mark(c.get_id(), mark)
    
    for s in students:
        s.caculate_gpa(courses)

    students.sort(key=lambda s: s.get_gpa(), reverse=True)
    return students, courses

def display_curses(stdscr, students):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== Student ranking by GPA ===")

    for row, s in enumerate(students, start=2):
        stdscr.addstr(row, 0, f"{s.get_id()} - {s.get_name()}: GPA = {s.get_gpa():.2f}")

    stdscr.addstr(len(students) + 3, 0, "Press any key to exit!")
    stdscr.refresh()
    stdscr.getch()

def main():
    students, courses = input_data()
    curses.wrapper(display_curses, students)

if __name__ == "__main__":
    main()