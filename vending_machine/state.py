from abc import ABC, abstractmethod
from inventory import Inventory,Product
'''
IdleState — waiting for coin

HasMoneyState — coin inserted

DispensingState — product is selected and being dispensed

ReturnChangeState - return the change to user

'''

class State(ABC):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    @abstractmethod
    def insert_coin(self, coin):
        pass

    @abstractmethod
    def select_product(self, product):
        pass

    @abstractmethod
    def dispense_product(self):
        pass

    @abstractmethod
    def cancel_transaction(self):
        pass

    @abstractmethod
    def return_change(self):
        pass

class IdleState(State):
    def insert_coin(self, coin):
       self.vending_machine.current_balance += coin.value
       print(f"Inserted ₹{coin.value}. Current balance: ₹{self.vending_machine.current_balance}")
       self.vending_machine.set_state(self.vending_machine.has_money_state)

    def select_product(self, product):
        print("Insert coin before selecting product")

    def dispense_product(self):
        print("Insert coin before selecting product")

    def cancel_transaction(self):
        print("No Transaction found")

    def return_change(self):
        print("No Transaction found")


class HasMoneyState(State):
    def insert_coin(self, coin):
        self.vending_machine.current_balance += coin.value
        print(f"Inserted ₹{coin.value}. Current balance: ₹{self.vending_machine.current_balance}")

    def select_product(self, product:Product):
        inventory:Inventory = self.vending_machine.inventory
        if inventory.is_available(product):
            if self.vending_machine.current_balance < product.price:
                print("Insufficient balance")
                return
            self.vending_machine.set_state(self.vending_machine.dispense_state)
            self.vending_machine.set_selected_product(product)
            self.vending_machine.current_state.dispense_product()
        else:
            print(f"product {product.name} not available")

    def dispense_product(self):
        print("choose product first")

    def cancel_transaction(self):
        print(f"Transaction called returning {self.vending_machine.current_balance}")
        self.vending_machine.set_state(self.vending_machine.return_change_state)
        self.vending_machine.current_state.return_change()

    def return_change(self):
        print("cancel the transaction to get refund")


class DispenseProductState(State):
    def insert_coin(self, coin):
        print("Transaction is in process. please wait")
    
    def select_product(self, product):
        print("Transaction is in process. please wait")
        
    def dispense_product(self):
        product = self.vending_machine.selected_product
        if product:
            print(f"Dispensing {product.name}")
            self.vending_machine.current_balance -=product.price
            self.vending_machine.inventory.update_quantity(product)
            self.vending_machine.set_selected_product(None)
        if self.vending_machine.current_balance >0:
            self.vending_machine.set_state(self.vending_machine.return_change_state)
            self.vending_machine.current_state.return_change()
        else:
            self.vending_machine.set_state(self.vending_machine.idle_state)

    def cancel_transaction(self):
        print("cannot cancel while dispensing")

    def return_change(self):
        print("product is dispensing")

class ReturnChangeState(State):
    def insert_coin(self, coin):
        print("refund in process")
    
    def select_product(self, product):
        print("refund in process")

    def dispense_product(self):
        print("refund in process")

    def cancel_transaction(self):
        print("no transaction found")

    def return_change(self):
        change_amount = self.vending_machine.current_balance
        if change_amount == 0:
            print("No amount to refund")
            self.vending_machine.set_state(self.vending_machine.idle_state)
            return
        print(f"Returning amount {change_amount}")
        self.vending_machine.current_balance = 0
        self.vending_machine.set_state(self.vending_machine.idle_state)


        


        
    

        



    
