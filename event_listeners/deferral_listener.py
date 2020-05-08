from .base import Base

from builders.deferral_builder import DeferralBuilder

class DeferralListener(Base):
  @property
  def event_builder(self):
    return DeferralBuilder
