from account import Account
class Bank:
    def __init__(self):
        self.accounts = {}
        self.pins = {}

    def add_account(self, card_number, account, pin):
        self.accounts[card_number] = account
        self.pins[card_number] = pin

    def validate_card(self, card, pin):
        return self.pins.get(card.card_number) == pin
    
    def get_account(self, card):
        return self.accounts.get(card.card_number)
    
    def process_transaction(self, transaction):
        transaction.execute()