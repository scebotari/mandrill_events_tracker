from .bounce_event_builder import BounceEventBuilder
from models.events.soft_bounce import SoftBounce

class SoftBounceBuilder(BounceEventBuilder):
  @classmethod
  def concrete_model(cls):
    return SoftBounce
