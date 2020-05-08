from fastapi import FastAPI, Depends

from database.mongo import MongoClient
from routers import mandrill, events

app = FastAPI()

app.include_router(
  mandrill.router,
  prefix='/mandrill',
  # Enforce signature check for all mandrill routes
  dependencies=[Depends(mandrill.check_signature)]
)

app.include_router(
  events.router,
  prefix='/events'
)

@app.on_event("startup")
def startup():
  # Establish mongodb connection on application startup
  # In production applications url, port and db mame should be taken from
  # environent variables
  MongoClient.connect('localhost', 27017, 'email_events')
