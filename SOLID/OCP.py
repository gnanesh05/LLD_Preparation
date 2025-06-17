from abc import ABC, abstractmethod

class SalaryCalculator:
    def calculate_salary(self, employee_type, base_salary):
        if employee_type == "fulltime":
            return base_salary * 1.2
        elif employee_type == "contractor":
            return base_salary * 1.1
        elif employee_type == "intern":
            return base_salary * 1.05
        else:
            return base_salary

class Employee(ABC):
    def __init__(self, base_salary):
        self.base_salary = base_salary
    
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTime(Employee):
    def calculate_salary(self):
        return self.base_salary*1.2
    
class Intern(Employee):
    def calculate_salary(self):
        return self.base_salary*1.05

