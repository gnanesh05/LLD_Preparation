from abc import ABC, abstractmethod

class TaxSlab(ABC):
    def __init__(self, min_amount, max_amount, rate):
        self.min_amount  = min_amount
        self.max_amount = max_amount
        self.rate = rate

    def calculateTax(self, income):
        pass

class ProgressiveSlab(TaxSlab):
    def __init__(self, min_amount, max_amount, rate):
        super().__init__(min_amount, max_amount, rate)
    
    def calculateTax(self, income):
        if income <= self.min_amount:
            return 0
        taxable_income = min(income, self.max_amount) - self.min_amount
        return (taxable_income * self.rate)/100
    

class TaxCalculator:
    def __init__(self,slabs:list[TaxSlab]):
        self.slabs = slabs

    def calculate_tax(self, income):
        total_tax = 0
        for slab in self.slabs:
            tax = slab.calculateTax(income)
            total_tax += tax
        return total_tax
    

class User:
    def __init__(self, name, income):
        self.name = name
        self.income = income


user = User("gnanesh", 1200000)
slabs = [
    ProgressiveSlab(0, 250000, 0),
    ProgressiveSlab(250000, 500000, 5),
    ProgressiveSlab(500000, 1000000, 20),
    ProgressiveSlab(1000000, float('inf'), 30)
]
calculator = TaxCalculator(slabs)
print(calculator.calculate_tax(user.income))
        
