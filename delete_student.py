def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    found = False

    # Open the file in read mode and delete the student record
    with open("students.txt", "r") as file:
        lines = file.readlines()
    
    with open("students.txt", "w") as file:
        for line in lines:
            student_data = line.strip().split(",")
            if student_data[0] == roll_no:
                print("Student record deleted successfully!")
                found = True
            else:
                file.write(line)
    
    if not found:
        print("Student not found.")
