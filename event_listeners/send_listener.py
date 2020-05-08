from .base import Base

from builders.send_builder import SendBuilder

class SendListener(Base):
  @property
  def event_builder(self):
    return SendBuilder
