def student_results():
    # Ask the user to enter student details
    name = input("Enter student name: ")
    coursework = float(input("Enter coursework mark out of 30: "))
    examination = float(input("Enter examination mark out of 70: "))

    # Calculate total mark
    total_mark = coursework + examination

    # Check whether the student has passed
    passed = total_mark >= 40

    # Display results
    print("\n--- Student Examination Results ---")
    print("Student Name:", name)
    print("Coursework Mark:", coursework)
    print("Examination Mark:", examination)
    print("Total Mark:", total_mark)
    print("Passed:", passed)


student_results()
