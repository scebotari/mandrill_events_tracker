from .event import Event

class Spam(Event):
  @staticmethod
  def name():
    return 'spam'
