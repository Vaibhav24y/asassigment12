def search_student():
    roll_no = input("Enter Roll No to search: ")
    found = False

    # Open the file in read mode and search for the student record
    with open("students.txt", "r") as file:
        for line in file:
            student_data = line.strip().split(",")
            if student_data[0] == roll_no:
                print("Student found!")
                print("Roll No:", student_data[0])
                print("Name:", student_data[1])
                found = True
                break
    
    if not found:
        print("Student not found.")
