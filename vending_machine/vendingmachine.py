from state import IdleState,HasMoneyState, DispenseProductState,ReturnChangeState
from enum import Enum
from inventory import Inventory,Product

class Coin(Enum):
    ONE = 1
    TWO = 2
    FIVE = 5
    TEN = 10
    TWENTY = 20


class VendingMachine:
    def __init__(self):
        self.inventory = Inventory()
        self.current_balance = 0
        self.selected_product = None

        self.idle_state = IdleState(self)
        self.has_money_state = HasMoneyState(self)
        self.dispense_state = DispenseProductState(self)
        self.return_change_state = ReturnChangeState(self)

        self.current_state = self.idle_state

    def set_state(self, state):
        self.current_state = state

    def set_selected_product(self, product):
        self.selected_product = product

    def insert_coin(self, coin:Coin):
        self.current_state.insert_coin(coin)

    def select_product(self, product):
        self.current_state.select_product(product)
    
    def cancel_transaction(self):
        self.current_state.cancel_transaction()