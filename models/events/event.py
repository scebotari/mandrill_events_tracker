from abc import ABC, abstractmethod
from datetime import datetime
from pydantic import BaseModel

class Event(ABC, BaseModel):
  # Use message foreign id to connect event to message. Thus we get rid of
  # querying the DB every time we save an event. Also in this case event and
  # message can be saved independently.
  message_foreign_id: str
  occured_at: datetime # Will automatically be converted from unix timestamp

  @staticmethod
  @abstractmethod
  def name():
    pass
