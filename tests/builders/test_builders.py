import tests.factories.mandrill_event_factory as mandrill

from builders.deferral_builder import DeferralBuilder
from builders.spam_builder import SpamBuilder
from builders.reject_builder import RejectBuilder
from builders.send_builder import SendBuilder
from builders.unsubscribe_builder import UnsubscribeBuilder
from builders.hard_bounce_builder import HardBounceBuilder
from builders.soft_bounce_builder import SoftBounceBuilder
from builders.click_builder import ClickBuilder
from builders.open_builder import OpenBuilder
from builders.message_builder import MessageBuilder

from models.events.deferral import Deferral
from models.events.spam import Spam
from models.events.reject import Reject
from models.events.send import Send
from models.events.unsubscribe import Unsubscribe
from models.events.hard_bounce import HardBounce
from models.events.soft_bounce import SoftBounce
from models.events.click import Click
from models.events.open import Open
from models.message import Message

def test_deferral_builder():
  payload = mandrill.DeferralFactory(_id='test-foreign-id')
  event = DeferralBuilder.from_madrill_payload(payload)

  assert type(event) is Deferral
  assert event.message_foreign_id == 'test-foreign-id'

def test_spam_builder():
  payload = mandrill.SpamFactory(_id='test-foreign-id')
  event = SpamBuilder.from_madrill_payload(payload)

  assert type(event) is Spam
  assert event.message_foreign_id == 'test-foreign-id'

def test_reject_builder():
  payload = mandrill.RejectFactory(_id='test-foreign-id')
  event = RejectBuilder.from_madrill_payload(payload)

  assert type(event) is Reject
  assert event.message_foreign_id == 'test-foreign-id'

def test_send_builder():
  payload = mandrill.SendFactory(_id='test-foreign-id')
  event = SendBuilder.from_madrill_payload(payload)

  assert type(event) is Send
  assert event.message_foreign_id == 'test-foreign-id'

def test_unsubscribe_builder():
  payload = mandrill.UnsubscribeFactory(_id='test-foreign-id')
  event = UnsubscribeBuilder.from_madrill_payload(payload)

  assert type(event) is Unsubscribe
  assert event.message_foreign_id == 'test-foreign-id'

def test_hard_bounce_builder():
  payload = mandrill.HardBounceFactory(
    _id='test-foreign-id',
    msg=mandrill.MsgFactory(diag='300')
  )
  event = HardBounceBuilder.from_madrill_payload(payload)

  assert type(event) is HardBounce
  assert event.message_foreign_id == 'test-foreign-id'
  assert event.code == '300'

def test_soft_bounce_builder():
  payload = mandrill.SoftBounceFactory(
    _id='test-foreign-id',
    msg=mandrill.MsgFactory(bounce_description='bad_email_address')
  )
  event = SoftBounceBuilder.from_madrill_payload(payload)

  assert type(event) is SoftBounce
  assert event.message_foreign_id == 'test-foreign-id'
  assert event.description == 'bad_email_address'

def test_click_builder():
  payload = mandrill.ClickFactory(_id='test-foreign-id')
  event = ClickBuilder.from_madrill_payload(payload)

  assert type(event) is Click
  assert event.message_foreign_id == 'test-foreign-id'

def test_open_builder():
  payload = mandrill.OpenFactory(_id='test-foreign-id')
  event = OpenBuilder.from_madrill_payload(payload)

  assert type(event) is Open
  assert event.message_foreign_id == 'test-foreign-id'

def test_message_builder():
  payload = mandrill.OpenFactory(_id='test-foreign-id')
  event = MessageBuilder.from_madrill_payload(payload)

  assert type(event) is Message
  assert event.foreign_id == 'test-foreign-id'
