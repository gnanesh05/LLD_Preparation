from Notification import Notification

class SMSNotification(Notification):
    def __init__(self):
        super().__init__("SMS")
    def send(self, to, message):
        print(f'Sending {self.type} to {to}: {message}')
    
class EmailNotification(Notification):
    def __init__(self):
        super().__init__("Email")
    def send(self, to, message):
        print(f'Sending {self.type} to {to}: {message}')
    
class PushNotification(Notification):
    def __init__(self):
        super().__init__("Push Notification")
    def send(self, to, message):
        print(f'Sending {self.type} to {to}: {message}')
