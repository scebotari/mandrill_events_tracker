class WebSocketPool:
  __instance = None

  def __init__(self):
    if WebSocketPool.__instance == None:
      self.__pool = []
      WebSocketPool.__instance = self

  @staticmethod
  def get_instance():
    if WebSocketPool.__instance == None:
      WebSocketPool()
    
    return WebSocketPool.__instance
  
  @staticmethod
  def connection_pool():
    return WebSocketPool.get_instance().__pool
  
  @staticmethod
  def connect(websocket):
    WebSocketPool.connection_pool().append(websocket)
  
  @staticmethod
  def disconnect(websocket):
    WebSocketPool.connection_pool().remove(websocket)

  @staticmethod
  async def broadcast(payload):
    for connection in WebSocketPool.connection_pool():
      # Broadcase json using send_text method, because starlette's send_json
      # method works only with primitive datatypes and does not handle datetime
      await connection.send_text(payload)
