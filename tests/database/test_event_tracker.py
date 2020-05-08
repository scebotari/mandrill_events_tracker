import pytest
import asyncio

from database.event_tracker import EventTracker
from tests.factories.event_factory import (
  DeferralFactory,
  SpamFactory,
  RejectFactory,
  SendFactory,
  UnsubscribeFactory,
  HardBounceFactory,
  SoftBounceFactory,
  ClickFactory,
  OpenFactory
)

@pytest.mark.asyncio
async def test_deferral_track(mongo_client):
  deferral = DeferralFactory.build(message_foreign_id='test-foreign-id')

  id = await EventTracker.track(deferral)
  result = await mongo_client.database().deferral_tracker.find_one({ '_id': id })

  assert type(result) is dict
  assert result['message_foreign_id'] == 'test-foreign-id'

@pytest.mark.asyncio
async def test_spam_track(mongo_client):
  spam = SpamFactory.build(message_foreign_id='test-foreign-id')

  id = await EventTracker.track(spam)
  result = await mongo_client.database().spam_tracker.find_one({ '_id': id })

  assert type(result) is dict
  assert result['message_foreign_id'] == 'test-foreign-id'

@pytest.mark.asyncio
async def test_reject_track(mongo_client):
  reject = RejectFactory.build(message_foreign_id='test-foreign-id')

  id = await EventTracker.track(reject)
  result = await mongo_client.database().reject_tracker.find_one({ '_id': id })

  assert type(result) is dict
  assert result['message_foreign_id'] == 'test-foreign-id'

@pytest.mark.asyncio
async def test_send_track(mongo_client):
  send = SendFactory.build(message_foreign_id='test-foreign-id')

  id = await EventTracker.track(send)
  result = await mongo_client.database().send_tracker.find_one({ '_id': id })

  assert type(result) is dict
  assert result['message_foreign_id'] == 'test-foreign-id'

@pytest.mark.asyncio
async def test_unsubscribe_track(mongo_client):
  unsubscribe = UnsubscribeFactory.build(message_foreign_id='test-foreign-id')

  id = await EventTracker.track(unsubscribe)
  result = await mongo_client.database().unsubscribe_tracker.find_one({ '_id': id })

  assert type(result) is dict
  assert result['message_foreign_id'] == 'test-foreign-id'

@pytest.mark.asyncio
async def test_soft_bounce_track(mongo_client):
  soft_bounce = SoftBounceFactory.build(code='500')

  id = await EventTracker.track(soft_bounce)
  result = await mongo_client.database().soft_bounce_tracker.find_one({ '_id': id })

  assert type(result) is dict
  assert result['code'] == '500'

@pytest.mark.asyncio
async def test_hard_bounce_track(mongo_client):
  hard_bounce = HardBounceFactory.build(code='500')

  id = await EventTracker.track(hard_bounce)
  result = await mongo_client.database().hard_bounce_tracker.find_one({ '_id': id })

  assert type(result) is dict
  assert result['code'] == '500'

@pytest.mark.asyncio
async def test_click_track(mongo_client):
  click = ClickFactory.build(url='example.com')

  id = await EventTracker.track(click)
  result = await mongo_client.database().click_tracker.find_one({ '_id': id })

  assert type(result) is dict
  assert result['url'] == 'example.com'

@pytest.mark.asyncio
async def test_open_track(mongo_client):
  open = OpenFactory.build(ip='localhost')

  id = await EventTracker.track(open)
  result = await mongo_client.database().open_tracker.find_one({ '_id': id })

  assert type(result) is dict
  assert result['ip'] == 'localhost'

