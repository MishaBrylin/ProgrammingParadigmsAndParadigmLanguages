class NotificationSystem:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer:
    def update(self, message):
        pass


class EmailNotification(Observer):
    def update(self, message):
        print("Sending email notification:", message)


class SMSNotification(Observer):
    def update(self, message):
        print("Sending SMS notification:", message)



notification_system = NotificationSystem()

email_notification = EmailNotification()
sms_notification = SMSNotification()

notification_system.add_observer(email_notification)
notification_system.add_observer(sms_notification)

notification_system.notify_observers("New notification!")