from .bounce_event import BounceEvent

class SoftBounce(BounceEvent):
  @staticmethod
  def name():
    return 'soft_bounce'