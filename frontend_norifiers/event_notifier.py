import json

from .web_socket_pool import WebSocketPool

class EventNotifier:
  @staticmethod
  async def notify(event):
    payload = { 'type': event.name(), **event.dict() }
    return await WebSocketPool.broadcast(json.dumps(payload, default=str))
