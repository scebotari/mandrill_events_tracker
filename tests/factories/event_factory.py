import factory

from datetime import datetime
from models.events import (
  open, click, deferral, soft_bounce, hard_bounce,
  spam, reject, send, unsubscribe
)
from .location_factory import LocationFactory
from .user_agent_info_factory import UserAgentInfoFactory

class EventFactory(factory.Factory):
  message_foreign_id = factory.Sequence(lambda n: f'foreign-id-{n}')
  occured_at = factory.LazyFunction(datetime.now)

class DeferralFactory(EventFactory):
  class Meta:
    model = deferral.Deferral

class SpamFactory(EventFactory):
  class Meta:
    model = spam.Spam

class RejectFactory(EventFactory):
  class Meta:
    model = reject.Reject

class SendFactory(EventFactory):
  class Meta:
    model = send.Send

class UnsubscribeFactory(EventFactory):
  class Meta:
    model = unsubscribe.Unsubscribe

class BounceEventFactory(EventFactory):
  code = 500
  description = 'bad_inbox'

class HardBounceFactory(BounceEventFactory):
  class Meta:
    model = hard_bounce.HardBounce

class SoftBounceFactory(BounceEventFactory):
  class Meta:
    model = soft_bounce.SoftBounce

class RecipientEventFactory(EventFactory):
  ip = factory.Faker('ipv4')
  user_agent = factory.Faker('user_agent')
  location = LocationFactory.build()
  user_agent_info = UserAgentInfoFactory.build()

class ClickFactory(RecipientEventFactory):
  class Meta:
    model = click.Click

  url = factory.Faker('url')

class OpenFactory(RecipientEventFactory):
  class Meta:
    model = open.Open
