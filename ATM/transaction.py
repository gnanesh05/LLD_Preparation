from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, transaction_id, account, amount):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount

    @abstractmethod
    def execute(self):
        pass

class DepositTrnsaction(Transaction):
    def __init__(self,transaction_id, account, amount):
        super().__init__(transaction_id, account, amount)
    
    def execute(self):
        return self.account.credit(self.amount)
    

class WithdrawlTransaction(Transaction):
    def __init__(self,transaction_id, account, amount):
        super().__init__(transaction_id, account, amount)
    
    def execute(self):
        return self.account.debit(self.amount) 
    
