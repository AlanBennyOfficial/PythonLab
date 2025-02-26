employee_name = input("Enter the employee name: ")
employee_id = input("Enter the employee ID: ")
employee_salary = input("Enter the employee salary: ")
basic = input("Enter base pay: ")
payback = input("Enter Payback: ")
daily_allowance = input("Enter daily allowance ")

net_salary = (basic + payback)*daily_allowance

print("Name = ", employee_name)
print("ID =",employee_id)
print("Salary = ",employee_salary)
print("Net Salary = ",net_salary)
