grades = {}

while True:
    print("\n1. Add a new student and grade")
    print("2. Update an existing student’s grade")
    print("3. Print all student grades")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        grades[name] = grade
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in grades:
            grade = input("Enter new grade: ")
            grades[name] = grade
        else:
            print("Student not found.")
    elif choice == "3":
        for name, grade in grades.items():
            print(f"{name}: {grade}")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

