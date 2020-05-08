from .mongo import MongoClient

class EventTracker:
  @classmethod
  async def track(cls, event):
    collection_name = f"{event.name()}_tracker"
    return await MongoClient.create(collection_name, event.dict())
