class Employee:
    def __init__(self, name, age, emp_id):
        self.name = name
        self.age = age
        self.emp_id = emp_id
    
    def display_info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Employee ID = {self.emp_id}")

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def display_info(self):
        return super().display_info()
    
    def calculate_salary(self, salary):
        return print(f"Salary = {salary}")

class PartTimeEmployee(Employee):
    def display_info(self):
        return super().display_info()
    
    def calculate_salary(self, salary):
        HourlyRate = input()
        return print(f"Salary = {salary*}")

class ContractEmployee(Employee):
    def display_info(self):
        return super().display_info()
    
    def calculate_salary(self, salary):
        return print(f"Salary = {salary}")
    
emp1 = FullTimeEmployee("Bob", 20, 911) 
emp1.display_info()
emp1.calculate_salary(5000)