from .event_builder import EventBuilder
from models.events.location import Location
from models.events.user_agent_info import UserAgentInfo

class RecipientEventBuilder(EventBuilder):
  @classmethod
  def convert_mandrill_payload(cls, payload):
    return {
      **super().convert_mandrill_payload(payload),
      'ip': payload.get('ip', ''),
      'user_agent': payload.get('user_agent', ''),
      'location': Location(**payload.get('location', {})),
      'user_agent_info': UserAgentInfo(**payload.get('user_agent_parsed', {}))
    }
