import threading
import datetime
from bank import Bank
from transaction import WithdrawlTransaction, DepositTrnsaction
from account import Account, Card

class CashDispenser:
    def __init__(self, cash_available):
        self.cash_available = cash_available
        self.lock = threading.Lock()

    def check_cash_available(self, amount):
        return self.cash_available >= amount
    
    def dispense_cash(self, amount):
        with self.lock:
            if self.check_cash_available(amount):
                self.cash_available -= amount
                print(f"Dispensed Amount - Rs.{amount}")
                return True
            return False

class Atm:
    def __init__(self,bank:Bank,dispenser:CashDispenser):
        self.bank = bank
        self.dispenser = dispenser
        self.current_card:Card = None
        self.current_account:Account = None
        self.transaction_counter = 0
        self.transaction_lock = threading.Lock()

    def insert_card(self, card:Card):
        self.current_card = card
        print(f"Inserted Card!")
    
    def input_pin(self,pin):
        if self.bank.validate_card(self.current_card, pin):
            self.current_account = self.bank.get_account(self.current_card)
            print("Card validated")
            return True
        print("Entered incorrent pin")
        return False
    
    def balance_enquiry(self):
        return self.current_account.get_balance()
    
    def withdraw_cash(self, amount):
        transaction = WithdrawlTransaction(self.generate_transaction_id(), self.current_account, amount)
        self.bank.process_transaction(transaction)
        self.dispenser.dispense_cash(amount)

    def deposit_cash(self, amount):
        transaction = DepositTrnsaction(self.generate_transaction_id(), self.current_account, amount)
        self.bank.process_transaction(transaction)

    def generate_transaction_id(self):
        with self.transaction_lock:
            self.transaction_counter +=1
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            return f"TXN{timestamp}{self.transaction_counter:010d}"
        



