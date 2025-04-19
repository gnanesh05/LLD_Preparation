from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name, base_rate):
        self.name = name
        self.base_rate = base_rate

    @abstractmethod
    def get_type(self):
        pass
    
    @abstractmethod
    def calculate_rental(self):
        pass

