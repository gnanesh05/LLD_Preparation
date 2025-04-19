from Vehicle import Vehicle

class Car(Vehicle):
    def get_type(self):
        return "Car"
    
    def calculate_rental(self, hours):
        return self.base_rate * hours


