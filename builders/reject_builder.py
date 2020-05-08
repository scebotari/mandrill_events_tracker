from .event_builder import EventBuilder
from models.events.reject import Reject

class RejectBuilder(EventBuilder):
  @classmethod
  def concrete_model(cls):
    return Reject
