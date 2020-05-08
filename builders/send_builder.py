from .event_builder import EventBuilder
from models.events.send import Send

class SendBuilder(EventBuilder):
  @classmethod
  def concrete_model(cls):
    return Send
