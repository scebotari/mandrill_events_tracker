from .event_builder import EventBuilder
from models.events.unsubscribe import Unsubscribe

class UnsubscribeBuilder(EventBuilder):
  @classmethod
  def concrete_model(cls):
    return Unsubscribe
