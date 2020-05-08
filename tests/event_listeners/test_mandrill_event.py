import pytest
import asyncio
from unittest.mock import patch

from event_listeners import mandrill_event
from event_listeners.click_listener import ClickListener
from event_listeners.hard_bounce_listener import HardBounceListener
from event_listeners.unknown_listener import UnknownListener
from tests.factories.mandrill_event_factory import ClickFactory, HardBounceFactory

@pytest.mark.asyncio
@patch.object(ClickListener, 'perform')
async def test_notify_click_event(mock):
  payload = ClickFactory.build()

  await mandrill_event.notify(payload)
  mock.assert_called()

@pytest.mark.asyncio
@patch.object(HardBounceListener, 'perform')
async def test_notify_hard_bounce_event(mock):
  payload = HardBounceFactory.build()

  await mandrill_event.notify(payload)
  mock.assert_called()

@pytest.mark.asyncio
@patch.object(UnknownListener, 'perform')
async def test_unknown_event(mock):
  await mandrill_event.notify({ 'event': 'full_open' })
  mock.assert_called()

@pytest.mark.asyncio
@patch.object(UnknownListener, 'perform')
async def test_empty_event(mock):
  await mandrill_event.notify({})
  mock.assert_called()
