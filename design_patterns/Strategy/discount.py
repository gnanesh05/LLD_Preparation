from abc import ABC, abstractmethod

#strategy interface
class DiscountStrategy(ABC):
    def __init__(self, discount=0):
        self.discount = discount
    @abstractmethod
    def make_discount(self,amount):
        pass

#concrete strategies
class PercentageDiscount(DiscountStrategy):
    def make_discount(self, amount):
        print(f'net amount - {amount - (amount*self.discount)/100}')

class FlatDiscount(DiscountStrategy):
    def make_discount(self, amount):
        print(f'net amount - {amount - self.discount}')

class NoDiscount(DiscountStrategy):
    def make_discount(self, amount):
        print(f'net amount - {amount}')


#context
class ShoppingCart():
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
    
    def checkout(self, amount):
        self.discount_strategy.make_discount(amount)


pdiscount = PercentageDiscount(10)
cart = ShoppingCart(pdiscount)
cart.checkout(200)