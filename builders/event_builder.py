from abc import ABC, abstractmethod
from datetime import datetime

class EventBuilder(ABC):
  @classmethod
  def from_madrill_payload(cls, payload):
    model = cls.concrete_model()
    return model(**cls.convert_mandrill_payload(payload))

  @classmethod
  def convert_mandrill_payload(cls, payload):
    return {
      'message_foreign_id': payload['_id'],
      'occured_at': payload.get('ts', datetime.now())
    }

  @classmethod
  @abstractmethod
  def concrete_model(cls):
    pass
