import os
import zipfile
from domains.student import Student, round_down
from domains.course import Course

def load_data():
    if os.path.exists("students.dat"):
        print("Found students.dat. Decompressing data...")
        with zipfile.ZipFile("students.dat", 'r') as zf:
            zf.extractall(".")
        
        students = {}
        courses = []

        if os.path.exists("courses.txt"):
            with open("courses.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        courses.append(Course(parts[0], parts[1], int(parts[2])))

        if os.path.exists("students.txt"):
            with open("students.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        students[parts[0]] = Student(parts[0], parts[1], parts[2])

        if os.path.exists("marks.txt"):
            with open("marks.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        s_id, c_id, mark = parts[0], parts[1], float(parts[2])
                        if s_id in students:
                            students[s_id].set_mark(c_id, mark)

        student_list = list(students.values())
        for s in student_list:
            s.calculate_gpa(courses)
        student_list.sort(key=lambda s: s.get_gpa(), reverse=True)
        
        print("Data successfully loaded from persistent files!")
        return student_list, courses

    return None, None

def save_text_files(students, courses):
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()}\n")

    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

    with open("marks.txt", "w", encoding="utf-8") as f:
        for s in students:
            for c_id, mark in s.get_marks().items():
                f.write(f"{s.get_id()},{c_id},{mark}\n")

    print("Data successfully written to text files.")

def compress_data():
    with zipfile.ZipFile("students.dat", 'w', zipfile.ZIP_DEFLATED) as zf:
        if os.path.exists("students.txt"):
            zf.write("students.txt")
        if os.path.exists("courses.txt"):
            zf.write("courses.txt")
        if os.path.exists("marks.txt"):
            zf.write("marks.txt")
    print("All files successfully compressed into students.dat.")

def input_data():
    students, courses = load_data()
    if students is not None and courses is not None:
        choice = input("Data loaded from storage. Do you want to re-enter new data? (y/n): ").strip().lower()
        if choice != 'y':
            return students, courses

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
        s.calculate_gpa(courses)

    students.sort(key=lambda s: s.get_gpa(), reverse=True)
    
    save_text_files(students, courses)
    compress_data()
    
    return students, courses