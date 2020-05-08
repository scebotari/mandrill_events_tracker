from .bounce_event_builder import BounceEventBuilder
from models.events.hard_bounce import HardBounce

class HardBounceBuilder(BounceEventBuilder):
  @classmethod
  def concrete_model(cls):
    return HardBounce
