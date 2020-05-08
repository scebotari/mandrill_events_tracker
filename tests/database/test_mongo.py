import pytest
import asyncio

@pytest.fixture(autouse=True)
async def clean_database(mongo_client):
  yield
  collections = await mongo_client.database().list_collection_names()
  for collection in collections:
    mongo_client.database()[collection].delete_many({})

@pytest.mark.asyncio
async def test_create(mongo_client):
  id = await mongo_client.create('test', { 'data': 'test' })
  record = await mongo_client.database().test.find_one({ '_id': id })

  assert type(record) is dict
  assert record['data'] == 'test'

@pytest.mark.asyncio
async def test_create_or_update(mongo_client):
  id = await mongo_client.create_or_update(
    'test',
    { 'id': 'test' },
    { 'data': 'testing' }
  )
  record = await mongo_client.database().test.find_one({ '_id': id })

  assert type(record) is dict
  assert record['data'] == 'testing'
  
  # Does not create a new record, when there's one existing for query
  id = await mongo_client.create_or_update(
    'test',
    { 'id': 'test' },
    { 'data': 'new data' }
  )
  record = await mongo_client.database().test.find_one({ '_id': id })
  count = await mongo_client.database().test.count_documents({})

  assert count == 1
  assert type(record) is dict
  assert record['data'] == 'new data'
