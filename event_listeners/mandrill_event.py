from .click_listener import ClickListener
from .open_listener import OpenListener
from .soft_bounce_listener import SoftBounceListener
from .hard_bounce_listener import HardBounceListener
from .deferral_listener import DeferralListener
from .spam_listener import SpamListener
from .reject_listener import RejectListener
from .send_listener import SendListener
from .unsubscribe_listener import UnsubscribeListener
from .unknown_listener import UnknownListener

async def notify(payload):
  # Fallback to and empty event type and to unknown event listetner afterwards
  event_type = payload.get('event', '')

  event_mapping = {
    'open': OpenListener,
    'click': ClickListener,
    'deferral': DeferralListener,
    'soft_bounce': SoftBounceListener,
    'hard_bounce': HardBounceListener,
    'spam': SpamListener,
    'reject': RejectListener,
    'send': SendListener,
    'unsub': UnsubscribeListener
  }
  listener = event_mapping.get(event_type, UnknownListener)
  await listener(payload).perform()

  return True
