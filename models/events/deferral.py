from .event import Event

class Deferral(Event):
  @staticmethod
  def name():
    return 'deferral'
