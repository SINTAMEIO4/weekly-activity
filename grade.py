def calculate_grade(mark):
    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"
mark = float(input("Enter the student's mark: "))
grade = calculate_grade(mark)
print(f"The student's grade is: {grade}")
