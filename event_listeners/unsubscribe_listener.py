from .base import Base

from builders.unsubscribe_builder import UnsubscribeBuilder

class UnsubscribeListener(Base):
  @property
  def event_builder(self):
    return UnsubscribeBuilder
