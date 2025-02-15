from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")


class SMSNotification(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "EMAIL":
            return EmailNotification()
        elif notification_type == "SMS":
            return SMSNotification()
        else:
            raise ValueError(f"Invalid notification type: {notification_type}")
