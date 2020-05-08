from abc import ABC, abstractmethod

from builders.message_builder import MessageBuilder
from database.event_tracker import EventTracker
from database.message_tracker import MessageTracker
from frontend_norifiers.event_notifier import EventNotifier

class Base(ABC):
  def __init__(self, payload):
    self.payload = payload
    self._message = None
    self._event = None

  async def perform(self):
    await MessageTracker.track(self.message)
    await EventTracker.track(self.event)
    await EventNotifier.notify(self.event)

    return True

  @property
  def message(self):
    if self._message is None:
      self._message = MessageBuilder.from_madrill_payload(self.payload)

    return self._message
  
  @property
  def event(self):
    if self._event is None:
      self._event = self.event_builder.from_madrill_payload(self.payload)

    return self._event

  @property
  @abstractmethod
  def event_builder(self):
    pass
