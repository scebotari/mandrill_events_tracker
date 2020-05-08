from .base import Base

from builders.hard_bounce_builder import HardBounceBuilder

class HardBounceListener(Base):
  @property
  def event_builder(self):
    return HardBounceBuilder
