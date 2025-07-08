'''
Entity:
    Card - card_number, pin
    Account - account_number, balance
    Transaction
        Withdrawl
        Deposit
    Bank - manages accounts, transactions, secures pin
    Cash Dispenser - dispense cash and track available
    ATM - entry point, manages sessions
'''
from atm import Atm, CashDispenser
from account import Account, Card
from bank import Bank

class Demo:
    @staticmethod
    def run():
        bank = Bank()
        cash_dispenser = CashDispenser(10000)
        atm = Atm(bank, cash_dispenser)

        account1  = Account("123456",1500)
        account2 = Account("78912",4000)
        card1 = Card("124578","1234")
        card2 = Card("56788","3456")
        bank.add_account(card1.get_card_number(), account1, card1.get_pin())
        bank.add_account(card2.get_card_number(), account2, card2.get_pin())

        
        atm.insert_card(card1)
        atm.input_pin("1234")
        atm.balance_enquiry()
        atm.withdraw_cash(500)


if __name__=='__main__':
    Demo.run()
