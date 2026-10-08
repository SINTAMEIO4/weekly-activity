def employee_salaries():
    #Create a dictionary named employees with five employees and salaries
    employees = {
        "Alice": 45000,
        "Brian": 52000,
        "Cynthia": 61000,
        "David": 48000,
        "Esther": 55000
    }
    #Display all employee names and salaries using a loop
    print("Employee Salaries:")
    for name, salary in employees.items():
        print(name, ":", salary)

    #Update the salary of one employee
    employees["Brian"] = 58000
    print("\nAfter updating Brian's salary:", employees["Brian"])

    #Add a new employee and salary
    employees["Felix"] = 50000
    print("After adding Felix:", employees)

    #Calculate and display the total salary payable
    total_salary = sum(employees.values())
    print("\nTotal Salary Payable:", total_salary)


employee_salaries()
