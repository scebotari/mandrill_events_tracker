from .base import Base

class UnknownListener(Base):
  async def perform(self):
    # Notify bug tracker (or whatever), that we got invalid (maybe new valid)
    # event from Mandrill to investigate this case further
    return False
  
  @property
  def event_builder(self):
    pass
