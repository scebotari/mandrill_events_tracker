from .event_builder import EventBuilder
from models.events.spam import Spam

class SpamBuilder(EventBuilder):
  @classmethod
  def concrete_model(cls):
    return Spam
