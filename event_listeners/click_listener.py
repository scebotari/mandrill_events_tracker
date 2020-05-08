from .base import Base

from builders.click_builder import ClickBuilder

class ClickListener(Base):
  @property
  def event_builder(self):
    return ClickBuilder
