import csv
import os
print(os.getcwd())
FILE_NAME = "students.csv"


# -----------------------------
# Initialize File (Create if not exists)
# -----------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Class", "Email"])
        print("File created successfully.")


# -----------------------------
# Add Student
# -----------------------------
def add_student():
    student_id = input("Enter Student ID: ")

    # Check duplicate ID
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == student_id:
                print("Student ID already exists!")
                return

    name = input("Enter Name: ")
    student_class = input("Enter Class: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, student_class, email])

    print("Student added successfully.")


# -----------------------------
# View All Students
# -----------------------------
def view_students():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        print("\n{:<10} {:<20} {:<10} {:<25}".format("ID", "Name", "Class", "Email"))
        print("-" * 65)
        next(reader)  # Skip header
        for row in reader:
            print("{:<10} {:<20} {:<10} {:<25}".format(*row))


# -----------------------------
# Search Student
# -----------------------------
def search_student():
    search_id = input("Enter Student ID to search: ")

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == search_id:
                print("\nStudent Found:")
                print("ID:", row[0])
                print("Name:", row[1])
                print("Class:", row[2])
                print("Email:", row[3])
                return

    print("Student not found.")


# -----------------------------
# Update Student
# -----------------------------
def update_student():
    update_id = input("Enter Student ID to update: ")
    updated = False
    rows = []

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for i in range(1, len(rows)):
        if rows[i][0] == update_id:
            print("Enter new details:")
            rows[i][1] = input("New Name: ")
            rows[i][2] = input("New Class: ")
            rows[i][3] = input("New Email: ")
            updated = True
            break

    if updated:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Student updated successfully.")
    else:
        print("Student not found.")


# -----------------------------
# Delete Student
# -----------------------------
def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    deleted = False
    rows = []

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [rows[0]]  # Keep header

    for row in rows[1:]:
        if row[0] != delete_id:
            new_rows.append(row)
        else:
            deleted = True

    if deleted:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)
        print("Student deleted successfully.")
    else:
        print("Student not found.")


# -----------------------------
# Main Menu
# -----------------------------
def main():
    initialize_file()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
