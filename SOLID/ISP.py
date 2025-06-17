from abc import ABC, abstractmethod
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class HumanWorker(Workable, Eatable):
    def work(self): print("Working")
    def eat(self): print("Eating")

class RobotWorker(Workable):
    def work(self): print("Working")


#instead having both abstract method in same class and force to do a dummy implementation of eat method in Robot

class PaymentProcessor(ABC):
    @abstractmethod
    def pay_credit_card(self): pass

    @abstractmethod
    def pay_upi(self): pass

    @abstractmethod
    def pay_paypal(self): pass

class CreditCard(ABC):
    @abstractmethod
    def pay_credit_card(self): pass

class UPI(ABC):
    @abstractmethod
    def pay_upi(self): pass

class PayPal(ABC):
    @abstractmethod
    def pay_paypal(self): pass



class CreditCardProcessor(CreditCard):
    def pay_credit_card(self): print("Paid with Credit Card")