def student_marks():

    # Create a list containing five subject marks
    marks = [65, 72, 58, 80, 69]

    # Display all the marks
    print("All Marks:", marks)

    # Calculate and display total marks
    total = sum(marks)
    print("Total Marks:", total)

    # Calculate and display average mark
    average = total / len(marks)
    print("Average Mark:", average)

    # Display the highest and lowest marks
    print("Highest Mark:", max(marks))
    print("Lowest Mark:", min(marks))

    # Modify the third subject mark
    marks[2] = 75

    # Display the updated list
    print("Updated Marks:", marks)


student_marks()


