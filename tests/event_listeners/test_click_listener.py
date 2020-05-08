import pytest
import asyncio
from asyncio import Future
from unittest.mock import patch

from event_listeners.click_listener import ClickListener
from database.event_tracker import EventTracker
from database.message_tracker import MessageTracker
from frontend_norifiers.event_notifier import EventNotifier

from tests.factories.mandrill_event_factory import ClickFactory

@pytest.mark.asyncio
@patch.object(EventTracker, 'track', return_value=asyncio.Future())
@patch.object(MessageTracker, 'track', return_value=asyncio.Future())
@patch.object(EventNotifier, 'notify', return_value=asyncio.Future())
async def test_click_listener(
  notifier_mock,
  message_tracker_mock,
  event_tracker_mock
):
  payload = ClickFactory.build()

  event_tracker_mock.return_value.set_result(None)
  message_tracker_mock.return_value.set_result(None)
  notifier_mock.return_value.set_result(None)

  await ClickListener(payload).perform()

  event_tracker_mock.assert_called()
  message_tracker_mock.assert_called()
  notifier_mock.assert_called()
