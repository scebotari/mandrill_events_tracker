from .base import Base

from builders.soft_bounce_builder import SoftBounceBuilder

class SoftBounceListener(Base):
  @property
  def event_builder(self):
    return SoftBounceBuilder
