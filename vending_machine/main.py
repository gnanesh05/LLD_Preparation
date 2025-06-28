'''Design a vending machine that supports inserting coins, selecting a product, dispensing it, and giving change.
 It should handle out-of-stock scenarios and return coins when a transaction is canceled'''

'''
Entity : Product, Inventory, Coins(Enum), State, CoinDispenser, VendingMachine
using state design pattern
'''

from vendingmachine import VendingMachine, Product, Coin

        
vending_machine = VendingMachine()

coke = Product("coke",20)
cake = Product("cake",30)
chips = Product("chips", 10)

vending_machine.inventory.add_product(coke,2)
vending_machine.inventory.add_product(chips,1)

vending_machine.insert_coin(Coin.TWENTY)

vending_machine.select_product(chips)

