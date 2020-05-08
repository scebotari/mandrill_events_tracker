from .base import Base

from builders.reject_builder import RejectBuilder

class RejectListener(Base):
  @property
  def event_builder(self):
    return RejectBuilder
