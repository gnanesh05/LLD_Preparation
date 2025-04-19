from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def send(self, to, message):
        pass

    