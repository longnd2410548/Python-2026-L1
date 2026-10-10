from domains.student import Student, round_down
from domains.course import Course

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