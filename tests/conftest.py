import pytest

from database.mongo import MongoClient

@pytest.fixture(scope='session')
def mongo_client():
  MongoClient.connect('localhost', 27017, 'email_events_test')
  return MongoClient

@pytest.fixture(autouse=True)
async def clean_database(mongo_client):
  yield
  collections = await mongo_client.database().list_collection_names()
  for collection in collections:
    mongo_client.database()[collection].delete_many({})
