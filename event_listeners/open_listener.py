from .base import Base

from builders.open_builder import OpenBuilder

class OpenListener(Base):
  @property
  def event_builder(self):
    return OpenBuilder
