from .mongo import MongoClient

class MessageTracker:
  @classmethod
  async def track(cls, message):
    return await MongoClient.create_or_update(
      "messages",
      { "foreign_id": message.foreign_id },
      message.dict()
    )
