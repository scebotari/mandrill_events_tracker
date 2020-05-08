from .event_builder import EventBuilder

class BounceEventBuilder(EventBuilder):
  @classmethod
  def convert_mandrill_payload(cls, payload):
    return {
      **super().convert_mandrill_payload(payload),
      # In documentation it is said, that 'msg' can be empty, handle such cases
      # setting empty values
      'code': payload.get('msg', {}).get('diag', ''),
      'description': payload.get('msg', {}).get('bounce_description', '')
    }
