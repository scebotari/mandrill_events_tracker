import factory

from datetime import datetime
from .location_factory import LocationFactory
from .user_agent_info_factory import UserAgentInfoFactory

class MsgFactory(factory.Factory):
  class Meta:
    model = dict

  _id = factory.Sequence(lambda n: f'foreign-id-{n}')
  ts = factory.Faker('date_time_this_month')
  email = factory.Faker('ascii_email')
  sender = factory.Faker('ascii_email')
  subject = 'Test subject'
  diag = 500
  bounce_description = 'bad_inbox'

class EventFactory(factory.Factory):
  class Meta:
    model = dict

  _id = factory.Sequence(lambda n: f'foreign-id-{n}')
  ts = factory.LazyFunction(datetime.now)
  msg = factory.LazyAttribute(lambda ev: MsgFactory.build(_id=ev._id))

class DeferralFactory(EventFactory):
  event = 'deferral'

class SpamFactory(EventFactory):
  event = 'spam'

class RejectFactory(EventFactory):
  event = 'reject'

class SendFactory(EventFactory):
  event = 'send'

class UnsubscribeFactory(EventFactory):
  event = 'unsub'

class HardBounceFactory(EventFactory):
  event = 'hard_bounce'

class SoftBounceFactory(EventFactory):
  event = 'soft_bounce'

class RecipientEventFactory(EventFactory):
  ip = factory.Faker('ipv4')
  user_agent = factory.Faker('user_agent')
  location = LocationFactory.build().dict()
  user_agent_parsed = UserAgentInfoFactory.build().dict()

class ClickFactory(RecipientEventFactory):
  event = 'click'

  url = factory.Faker('url')

class OpenFactory(RecipientEventFactory):
  event = 'open'
