from pymongo import ReturnDocument

import motor.motor_asyncio

class MongoClient:
  __database = None

  @staticmethod
  def connect(ip, port, db_name):
    client = motor.motor_asyncio.AsyncIOMotorClient(ip, port)
    MongoClient.__database = client[db_name]

  @staticmethod
  def database():
    return MongoClient.__database

  @staticmethod
  async def create(collection, document):
    result = await MongoClient.__database[collection].insert_one(document)
    return result.inserted_id

  @staticmethod
  async def create_or_update(collection, query, document):
    result = await MongoClient.__database[collection].find_one_and_update(
      query,
      { '$set': document },
      upsert=True,
      return_document=ReturnDocument.AFTER
    )

    return result['_id']
