from .recipient_event import RecipientEvent

class Open(RecipientEvent):
  @staticmethod
  def name():
    return 'open'
