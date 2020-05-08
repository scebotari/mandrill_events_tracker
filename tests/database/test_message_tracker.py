import pytest
import asyncio

from database.message_tracker import MessageTracker
from models.message import Message
from tests.factories.message_factory import MessageFactory

@pytest.mark.asyncio
async def test_track(mongo_client):
  message = MessageFactory.build(foreign_id='test')

  id = await MessageTracker.track(message)
  result = await mongo_client.database().messages.find_one({})

  assert type(result) is dict
  assert result['foreign_id'] == 'test'

  # Does not create more messages with the same foreign ID
  await MessageTracker.track(message)
  count = await mongo_client.database().messages.count_documents(
    { 'foreign_id': 'test' }
  )

  assert count == 1
