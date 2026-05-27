database = []
while True:

    print("\n\nwelcome to the Student Database Management System!!\n")
    print("----------------------------------------------------------------------\n")
    print("Select an option from the Menu below:\n")
    print("1. Add a student to the database\n")
    print("2. Display all students in the database\n")
    print("3. Search for a student by ID\n")
    print("4. Update a student's information\n")
    print("5. Delete a student from the database\n")
    print("6. Display subjects offered\n")
    print("7. delete all students from the database\n")
    print("8. Exit\n")
    print("----------------------------------------------------------------------\n")

    choice = int(input("Enter your choice from the menu:\n"))  
    
    match choice:
        case 1:

            print("You have selected to add a student to the database.\n")
            name = input("Enter the student's name: ")
            id = int(input("Enter the student's ID: "))
            age = int(input("Enter the student's age: "))
            grade = input("Enter the student's grade: ")
            subject = input("Enter the student's subject: ")
            dob = input("Enter the student's date of birth (DD/MM/YYYY): ")
            student = {
                "name": name,
                "id": id,
                "age": age,
                "grade": grade,
                "subject": subject,
                "dob": dob
            }
            database.append(student)
            print(f"{name} has been added to the database.\n")  
        case 2:
            print("You have selected to display all students in the database.\n")
            for student in database:
                print(f"Name: {student['name']}, ID: {student['id']}, Age: {student['age']}, Grade: {student['grade']}, Subject: {student['subject']}, DOB: {student['dob']}")  
        case 3:
            print("You have selected to search for a student by ID.\n")
            search_id = int(input("Enter the student's ID to search: "))
            found_students = [student for student in database if student['id'] == search_id]
            if found_students:
                for student in found_students:
                    print(f"Name: {student['name']}, ID: {student['id']}, Age: {student['age']}, Grade: {student['grade']}, Subject: {student['subject']}, DOB: {student['dob']}")  
            else:
                print(f"No student found with ID: {search_id}\n")
        case 4:
            print("You have selected to update a student's information.\n")
            update_id = int(input("Enter the student's ID to update: "))
            for student in database:
                if student['id'] == update_id:
                    print(f"Current information for {student['name']}: Age: {student['age']}, Grade: {student['grade']}, Subject: {student['subject']}, DOB: {student['dob']}")
                    student['age'] = int(input("Enter the new age: "))
                    student['grade'] = input("Enter the new grade: ")
                    student['subject'] = input("Enter the new subject: ")
                    student['dob'] = input("Enter the new date of birth (DD/MM/YYYY): ")
                    print(f"{student['name']}'s information has been updated.\n")
                    break
            else:
                print(f"No student found with ID: {update_id}\n")
        case 5:
            print("You have selected to delete a student from the database.\n")
            delete_id = int(input("Enter the student's ID to delete: "))
            for student in database:
                if student['id'] == delete_id:
                    database.remove(student)
                    print(f"{student['name']} has been deleted from the database.\n")
                    break
            else:
                print(f"No student found with ID: {delete_id}\n")
        case 6:
            print("You have selected to display subjects offered.\n")
            subjects = set(student['subject'] for student in database)
            for subject in subjects:
                print(subject)
        case 7:
            print("You have selected to delete all students from the database.\n")
            database.clear()
            print("All students have been deleted from the database.\n")
        case 8:
            break
        case _: 
            print("Invalid choice. Please select a valid option from the menu.\n")
