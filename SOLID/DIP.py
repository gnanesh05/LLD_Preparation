'''
High-level modules should not depend on low-level modules.
Both should depend on abstractions.

Abstractions should not depend on details.
Details should depend on abstractions.

'''
from abc import ABC, abstractmethod

class SwitchableDevice(ABC):
    @abstractmethod
    def turn_on(self): pass

class LightBulb(SwitchableDevice):
    def turn_on(self):
        print("LightBulb: ON")

class Fan(SwitchableDevice):
    def turn_on(self):
        print("Fan: ON")

class Switch:
    def __init__(self, device: SwitchableDevice):
        self.device = device

    def operate(self):
        self.device.turn_on()

'''
| Principle | Purpose                                    | Example Domain                        |
| --------- | ------------------------------------------ | ------------------------------------- |
| SRP       | One class = One reason to change           | Invoice generation system             |
| OCP       | Extend without modifying                   | Payment gateway                       |
| LSP       | Subtypes must behave like their parent     | UI Components / Widgets               |
| ISP       | Clients shouldn’t depend on unused methods | Multifunction device (print/scan/fax) |
| DIP       | Rely on abstractions not concrete classes  | Database, logging, payment            |
'''
