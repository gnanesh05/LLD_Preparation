from abc import ABC , abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_no):
        self.card_no = card_no

    def pay(self, amount):
        print(f"payed {amount}")

    def refund(self, amount):
        print(f"refund {amount}")

class UPI(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"payed {amount}")

    def refund(self, amount):
        print(f"refund {amount}")

class NetBanking(PaymentMethod):
    def __init__(self, acc_no):
        self.acc_no = acc_no

    def pay(self, amount):
        print(f"payed {amount}")

    def refund(self, amount):
        print(f"refund {amount}")