def employee_salary():

    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: "))
    deduction = float(input("Enter monthly deduction: "))

    housing_allowance = basic_salary * 10 / 100
    gross_salary = basic_salary + housing_allowance
    net_salary = gross_salary - deduction

    print("Employee Name:", name)
    print("Basic Salary:", basic_salary)
    print("Housing Allowance:", housing_allowance)
    print("Gross Salary:", gross_salary)
    print("Deduction:", deduction)
    print("Net Salary:", net_salary)


employee_salary()






