from .event import Event

class Unsubscribe(Event):
  @staticmethod
  def name():
    return 'unsubscribe'
