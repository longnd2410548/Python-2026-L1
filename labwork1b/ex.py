students = []
courses = []
marks = {}

def input_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        sid = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        students.append({"id": sid, "name": name, "dob": dob})

def input_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        cid = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append({"id": cid, "name": name})

def input_marks():
    cid = input("Enter course id to input marks: ")
    for student in students:
        mark = float(input(f"Enter mark for {student['name']}: "))
        if cid not in marks:
            marks[cid] = {}
        marks[cid][student['id']] = mark

def list_courses():
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_marks():
    cid = input("Enter course id: ")
    if cid in marks:
        for sid, mark in marks[cid].items():
            print(f"Student ID: {sid}, Mark: {mark}")

def main():
    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            show_marks()
        elif choice == '7':
            break

if __name__ == "__main__":
    main()
    