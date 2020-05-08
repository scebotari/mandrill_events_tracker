from event_listeners import mandrill_event

async def process_events(batch):
  for mandrill_event_payload in batch:
    await mandrill_event.notify(mandrill_event_payload)
