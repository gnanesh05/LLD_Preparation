class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product:Product, quantity):
        self.products[product] = quantity
    
    def get_product(self, product):
        self.products.get(product, 0)

    def update_product(self, product:Product, quantity):
        self.products[product] = [quantity]

    def update_quantity(self, product:Product):
        self.products[product] -=1
    
    def remove_product(self, product:Product):
        del self.products[product]

    def is_available(self, product:Product):
        return product in self.products and self.products[product] > 0
    
    def show_products(self):
        for product, quantity in self.products.items():
            print(f"Product - {product.name} Price - {product.price} Quanity - {quantity}")
