from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocket
from starlette.endpoints import WebSocketEndpoint

from frontend_norifiers.web_socket_pool import WebSocketPool
from frontend_norifiers.event_notifier import EventNotifier

router = APIRouter()

@router.get("/notifications")
async def get():
  return HTMLResponse("""
    <!DOCTYPE html>
    <html>
      <head>
        <title>Chat</title>
      </head>
      <body>
        <h2>Events:</h2>
        <ul id='events'>
        </ul>
        <script>
          var ws = new WebSocket("ws://localhost:8000/events/ws");
          ws.onmessage = function(event) {
            var data = JSON.parse(event.data)
            var events = document.getElementById('events')
            var message = document.createElement('li')
            var content = document.createTextNode(data['type'])
            message.appendChild(content)
            events.appendChild(message)
          };
          function sendMessage(event) {
            var input = document.getElementById("messageText")
            ws.send(input.value)
            input.value = ''
            event.preventDefault()
          }
        </script>
      </body>
    </html>
  """)

@router.websocket_route("/ws")
class WebSocketConnector(WebSocketEndpoint):
  async def on_connect(self, websocket: WebSocket) -> None:
    await websocket.accept()
    WebSocketPool.connect(websocket)

  async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
    WebSocketPool.disconnect(websocket)

from tests.factories.event_factory import ClickFactory
@router.get("/test")
async def test():
  await EventNotifier.notify(ClickFactory.build())
