from .recipient_event_builder import RecipientEventBuilder
from models.events.open import Open

class OpenBuilder(RecipientEventBuilder):
  @classmethod
  def concrete_model(cls):
    return Open
