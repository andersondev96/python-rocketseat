from abc import ABC, abstractmethod

class NotificationSender(ABC):

  @abstractmethod
  def send_notification(self, message: str) -> None: pass

  # Definir a regra de construção

class EmailNotificationSender(NotificationSender):

  def send_notification(self, message: str) -> None:
    print(f'Email message - {message}')

class SMSNotificationSender(NotificationSender):

  def send_notification(self, message: str) -> None:
    print(f'SMS message - {message}')

class Notificator:
  def __init__(self, notification_send: NotificationSender) -> None:
    self.__notification_send = notification_send

  def send(self, message: str) -> None:
    # Validação de dados
    self.__notification_send.send_notification(message)

obj = Notificator(SMSNotificationSender())
obj.send('Ola Mundo')