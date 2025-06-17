from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, plate_number):
        self.plate_number = plate_number
    
    @abstractmethod
    def get_spot_size(self):
        pass


class Bike(Vehicle):
    def get_spot_size(self):
        return "small"
    
class Car(Vehicle):
    def get_spot_size(self):
        return "medium"

class Truck(Vehicle):
    def get_spot_size(self):
        return "large"