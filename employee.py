"""
employee_status.py
This program records an employee's details, including their active
status as a Boolean value, and displays all information using
f-string formatting. It also demonstrates converting a number to a
string with str() before concatenation.
"""
employee_name = "Judith"
employee_age = 20
employee_salary = 45000.0
is_active = True  # Boolean value for active status

print(f"Employee Name: {employee_name}")
print(f"Age: {employee_age}")
print(f"Salary: {employee_salary}")
print(f"Active Status: {is_active}")


salary_message = "Salary is KSh " + str(employee_salary)
print(salary_message)
