from .event import Event

class Reject(Event):
  @staticmethod
  def name():
    return 'reject'
