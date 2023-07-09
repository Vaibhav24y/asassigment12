def add_student():
    try:
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        # Perform any necessary validations

        # Open a file in append mode and write the student record
        with open("students.txt", "a") as file:
            file.write(f"{roll_no},{name}\n")
        
        print("Student added successfully!")
    except Exception as e:
        print("An error occurred:", str(e))
