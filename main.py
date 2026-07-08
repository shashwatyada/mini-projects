def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    course = input("Enter Course: ")

    with open("students.txt", "a") as f:
        f.write(f"{name},{roll},{course}\n")

    print("Student Added Successfully!")

def view_students():
    try:
        with open("students.txt", "r") as f:
            data = f.readlines()
            for line in data:
                print(line.strip())
    except:
        print("No records found.")

def menu():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid Choice")

menu()