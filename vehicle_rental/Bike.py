from Vehicle import Vehicle

class Bike(Vehicle):
    def get_type(self):
        return "Bike"
    
    def calculate_rental(self,hours):
        return self.base_rate * hours + 10

    