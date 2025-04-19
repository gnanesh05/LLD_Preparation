from payment_processor import User,PaymentMethod, PaymentProcessor
from payment_method import CreditCard


user = User("Alice")
payment_method = CreditCard("1234-5678-9876-5432")
processor = PaymentProcessor()

payment = processor.process_payment(user, payment_method, 500)
processor.process_refund(payment)