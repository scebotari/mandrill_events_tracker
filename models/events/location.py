from pydantic import BaseModel

class Location(BaseModel):
  country_short: str = None
  country_long: str = None
  region: str = None
  city: str = None
  postal_code: str = None
  timezone: str = None
  latitude: float = None
  longitude: float = None

