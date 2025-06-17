from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):pass

#objects
class EmailObserver(Observer):
    def update(self, message):
        print(f'Email received {message} ')

class SMSObserver(Observer):
    def update(self, message):
        print(f'SMS received {message} ')

#subject
class NewsAgency():
    def __init__(self):
        self.subscribers = []

    def subscribe(self,observer:Observer):
        self.subscribers.append(observer)

    def unsubscribe(self,observer:Observer):
        self.subscribers.remove(observer)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


agency = NewsAgency()

email_sub = EmailObserver()
sms_sub = SMSObserver()

agency.subscribe(email_sub)
agency.subscribe(sms_sub)

agency.notify("hello everyone")
