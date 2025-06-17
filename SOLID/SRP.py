class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary * 1.2  # Bonus

    def generate_report(self):
        print(f"Employee: {self.name}, Salary: {self.calculate_salary()}")


class EmployeeSRP:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
class CalculateSalary:
    def calculate_bonus(self, employee: Employee):
        return employee.base_salary*1.2

class ReportService:
    def generate_employee_report(self, employee:Employee):
        obj = CalculateSalary()
        print(f"Employee: {employee.name}, Salary: {obj.calculate_bonus(employee)}")


