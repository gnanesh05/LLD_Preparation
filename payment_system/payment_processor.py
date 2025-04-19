import uuid
from payment_method import PaymentMethod
class User:
    def __init__(self, name):
        self.name = name

class Payment:
    def __init__(self, id, user: User , paymentMethod:PaymentMethod, amount, status="processed"):
        self.id = id
        self.amount = amount
        self.status = status
        self.paymentMethod: paymentMethod
        self.user = user

    def get_status(self):
        print(self.status)

    def set_status(self,status):
        self.status = status




class PaymentProcessor:
    
    def process_payment(self, user:User, paymentMethod: PaymentMethod, amount:float ):
        return Payment(uuid.uuid1(), user, paymentMethod, amount)
    
    def process_refund(self, payment: Payment):
        payment.set_status("refund")
        payment.get_status()