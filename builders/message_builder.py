from datetime import datetime

from models.message import Message

class MessageBuilder:
  @classmethod
  def from_madrill_payload(cls, payload):
    return Message(**cls.convert_mandrill_payload(payload))

  @classmethod
  def convert_mandrill_payload(cls, payload):
    # Fallback to blank message payload, if it's blank
    message_payload = payload.get('msg', {})

    return {
      'foreign_id': message_payload['_id'],
      'sent_at': message_payload['ts'],
      'recipient': message_payload['email'],
      'sender': message_payload['sender'],
      'subject': message_payload['subject']
    }
