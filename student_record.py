def student_record():
    #Create a dictionary named student
    student = {
        "reg_number": "S2026001",
        "name": "Judith",
        "course": "Computer Science",
        "year": 2
    }

    #Display the student's name and course using their keys
    print("Student Name:", student["name"])
    print("Course:", student["course"])

    #Change the student's year of study
    student["year"] = 3

    #Add an email address to the dictionary
    student["email"] = "judith@gmail.com"

    #Display the complete updated dictionary
    print("Updated Record:", student)


student_record()
