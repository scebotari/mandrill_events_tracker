from .bounce_event import BounceEvent

class HardBounce(BounceEvent):
  @staticmethod
  def name():
    return 'hard_bounce'
