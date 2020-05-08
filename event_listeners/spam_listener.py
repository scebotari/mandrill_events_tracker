from .base import Base

from builders.spam_builder import SpamBuilder

class SpamListener(Base):
  @property
  def event_builder(self):
    return SpamBuilder
