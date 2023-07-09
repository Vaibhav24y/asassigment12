from Student_management import menu
from Student_management import add_student
from Student_management import search_student
from Student_management import update_student
from Student_management import delete_student

while True:
    menu.display_menu()
    choice = menu.get_user_choice()

    if choice == 1:
        add_student.add_student()
    elif choice == 2:
        search_student.search_student()
    elif choice == 3:
        update_student.update_student()
    elif choice == 4:
        delete_student.delete_student()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please select a valid option.")
