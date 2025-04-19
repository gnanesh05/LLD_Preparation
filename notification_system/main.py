from SMS import SMSNotification, EmailNotification, PushNotification

notifs = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notif in notifs:
    notif.send("user@example.com", "Hello from our app!")