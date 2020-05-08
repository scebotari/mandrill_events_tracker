from .event import Event
from .location import Location
from .user_agent_info import UserAgentInfo

class RecipientEvent(Event):
  ip: str
  user_agent: str
  location: Location = None
  user_agent_info: UserAgentInfo = None
