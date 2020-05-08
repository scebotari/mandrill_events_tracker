import factory

from datetime import datetime, timedelta
from models.message import Message 

class MessageFactory(factory.Factory):
  class Meta:
    model = Message

  foreign_id = factory.Sequence(lambda n: f'foreign-id-{n}')
  sent_at = factory.Faker('date_time_this_month')
  recipient = factory.Faker('ascii_email')
  sender = factory.Faker('ascii_email')
  subject = 'Test subject'
