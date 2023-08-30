students = []


def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")
    students.append({"name": name, "age": age, "grade": grade})
    print("Student added successfully!")


def view_students():
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")


def search_student(name):
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            return
    print("Student not found.")


while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_name = input("Enter student's name to search: ")
        search_student(search_name)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
