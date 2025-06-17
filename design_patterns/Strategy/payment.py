from abc import ABC, abstractmethod

#stratefy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

#concrete strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'paid {amount} via credit card')

class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'paid {amount} via UPI')

#context
class PaymentProcessor():
    def __init__(self, strategy:PaymentStrategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


creditcard = CreditCardPayment()
paymentProcessor = PaymentProcessor(creditcard)
paymentProcessor.make_payment(1000)

