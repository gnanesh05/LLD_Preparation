'''
lets take the example of notification system we're going to abstract instantiation logic from client
'''
from abc import ABC, abstractmethod

# Step 1: Common Interface
class Notification(ABC):
    @abstractmethod
    def notify(self, message): pass

# Step 2: Concrete Classes
class EmailNotification(Notification):
    def notify(self, message):
        print(f"Email: {message}")

class SMSNotification(Notification):
    def notify(self, message):
        print(f"SMS: {message}")

class PushNotification(Notification):
    def notify(self, message):
        print(f"Push: {message}")

# Step 3: Factory
class NotificationFactory:
    @staticmethod
    def get_notification(channel: str) -> Notification:
        if channel == "email":
            return EmailNotification()
        elif channel == "sms":
            return SMSNotification()
        elif channel == "push":
            return PushNotification()
        else:
            raise ValueError("Unknown notification type")

# Step 4: Usage
notification = NotificationFactory.get_notification("email")
notification.notify("Hello!")



'''
example 2 - Vehicle factory
'''

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving car!")

class Bike(Vehicle):
    def drive(self):
        print("Driving Bike")

class VehicleFactory:
    @staticmethod
    def get_driving_notification(type:str) -> Vehicle:
        if type == "car":
            return Car()
        if type == "bike":
            return Bike()
        else:
            raise ValueError("invalid type")
        
vehicle = VehicleFactory.get_driving_notification("car")
vehicle.drive()
    
