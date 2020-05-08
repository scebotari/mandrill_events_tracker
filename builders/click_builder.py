from .recipient_event_builder import RecipientEventBuilder
from models.events.click import Click

class ClickBuilder(RecipientEventBuilder):
  @classmethod
  def convert_mandrill_payload(cls, payload):
    return {
      **super().convert_mandrill_payload(payload),
      'url': payload['url']
    }

  @classmethod
  def concrete_model(cls):
    return Click
