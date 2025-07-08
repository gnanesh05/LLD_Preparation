class Account:
    def __init__(self,account_number:str, balance:int):
        self.account_number = account_number
        self.balance = balance

    def get_account_number(self):
        return self.account_number
    
    def get_balance(self):
        return self.balance
    
    def credit(self, amount:int):
        self.balance += amount
        return True
    
    def debit(self, amount:int):
        if(self.balance >=amount):
            self.balance -= amount
            return True
        return False

class Card:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin

    def get_card_number(self):
        return self.card_number
    
    def get_pin(self):
        return self.pin
    

        
