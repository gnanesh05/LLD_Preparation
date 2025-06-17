'''
Problem Statement
You are designing a furniture store system that sells different styles of furniture:

Modern

Victorian

Each furniture style includes the following products:

Chair

Sofa

'''
from abc import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit_on(self):pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self):pass

class ModernChair(Chair):
    def sit_on(self):
        print("Sitting on a modern chair")

class VictorianChair(Chair):
    def sit_on(self):
        print("Sitting on a victorian chair")

class ModernSofa(Sofa):
    def lie_on(self):
        print("Lying on a modern sofa")

class VictorianSofa(Sofa):
    def lie_on(self):
        print("Lying on a victorian sofa")


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair: pass

    @abstractmethod
    def create_sofa(self) -> Sofa: pass

class VictorianFactory(FurnitureFactory):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()
    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()
    
class ModernFactory(FurnitureFactory):
    def create_chair(self) -> ModernChair:
        return ModernChair()
    def create_sofa(self) -> ModernSofa:
        return ModernSofa()
    

def create_order(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    chair.sit_on()
    sofa.lie_on()

factory = VictorianFactory()
create_order(factory)