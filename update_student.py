def update_student():
    roll_no = input("Enter Roll No to update: ")
    updated_name = input("Enter updated Name: ")
    found = False

    # Open the file in read mode and update the student record
    with open("students.txt", "r") as file:
        lines = file.readlines()
    
    with open("students.txt", "w") as file:
        for line in lines:
            student_data = line.strip().split(",")
            if student_data[0] == roll_no:
                file.write(f"{roll_no},{updated_name}\n")
                print("Student record updated successfully!")
                found = True
            else:
                file.write(line)
    
    if not found:
        print("Student not found.")
