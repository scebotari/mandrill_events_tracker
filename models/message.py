from pydantic import BaseModel

from datetime import datetime

class Message(BaseModel):
  foreign_id: str
  sent_at: datetime
  recipient: str
  sender: str
  subject: str = ''
