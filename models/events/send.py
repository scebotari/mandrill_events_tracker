from .event import Event

class Send(Event):
  @staticmethod
  def name():
    return 'send'
