import os
import pickle
import gzip
from domains.student import Student, round_down
from domains.course import Course

def load_data():
    if os.path.exists("students.dat"):
        print("Found students.dat. Decompressing and unpickling data...")
        try:
            with gzip.open("students.dat", "rb") as f:
                data = pickle.load(f)
            students = data.get("students", [])
            courses = data.get("courses", [])
            print("Data successfully loaded using pickle!")
            return students, courses
        except Exception as e:
            print(f"Error loading data: {e}")
    return None, None

def save_data(students, courses):
    data = {
        "students": students,
        "courses": courses
    }
    with gzip.open("students.dat", "wb") as f:
        pickle.dump(data, f)
    print("Data successfully pickled and compressed into students.dat.")

def input_data():
    students, courses = load_data()
    if students and courses:
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
    
    save_data(students, courses)
    
    return students, courses