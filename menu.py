def display_menu():
    print("Student Management System")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def get_user_choice():
    choice = input("Enter your choice (1-5): ")
    return int(choice)
