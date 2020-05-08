from .recipient_event import RecipientEvent

class Click(RecipientEvent):
  url: str

  @staticmethod
  def name():
    return 'click'
