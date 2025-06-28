from abc import ABC, abstractmethod
import uuid
'''
design a Restaurant listing aplication where user can make orders and customize their orders by adding additional stuffs like toppings, salads etc
'''

class Food(ABC):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    def supports_customization(self):
        return True


class Burger(Food):

    def get_description(self):
        return "Burger"
    
    def get_price(self):
        return 100
    
class Pizza(Food):

    def get_description(self):
        return "Pizza"
    
    def get_price(self):
        return 150

class MangoDrink(Food):
    def get_description(self):
        return "Mango Drink"
    def get_price(self):
        return 30
    def supports_customization(self):
        return False

#using decorator pattern to dynamically added additional attributes to object with creating sub classes
class ToppingDecorator(Food):
    def __init__(self, food:Food):
        if not food.supports_customization():
            raise Exception(f"{food.get_description()} doesn't support any customization")
        self._food = food
    
    def get_description(self):
        return self._food.get_description()
    
    def get_price(self):
        return self._food.get_price()
    

class ExtraCheese(ToppingDecorator):
    def get_description(self):
        return self._food.get_description() + "Extra Cheese"
    
    def get_price(self):
        return self._food.get_price() + 10
    
class ExtraSalad(ToppingDecorator):
    def get_description(self):
        return self._food.get_description() + "Extra Salad"

    def get_price(self):
        return self._food.get_price() + 10

class User():
    def __init__(self, name):
        self.name = name
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
   
class Order():
    def __init__(self,user):
        self.id = uuid.uuid1()
        self.user = user
        self.items = []

    # can be improved to make {item_name : quantity : price}
    def add_item(self,food):
        self.items.append(food)
    
    def remove_item(self, food):
        self.items.remove(food)

    def print_summary(self):
        print(f"\n🧾 Order Summary for {self.user.name} (Order ID: {self.id})")
        total = 0
        for item in self.items:
            print(f" - {item.get_description()} : ₹{item.get_price()}")
            total += item.get_price()
        print(f"Total Amount: ₹{total}\n")



user = User("gnanesh")
order = Order(user)

try:
    burger = ExtraCheese(Burger())
    pizza = ExtraSalad(ExtraCheese(Pizza()))
except Exception as e:
    print(e)

order.add_item(burger)
order.add_item(pizza)

user.place_order(order)
order.print_summary()