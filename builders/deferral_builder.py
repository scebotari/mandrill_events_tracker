from .event_builder import EventBuilder
from models.events.deferral import Deferral

class DeferralBuilder(EventBuilder):
  @classmethod
  def concrete_model(cls):
    return Deferral
