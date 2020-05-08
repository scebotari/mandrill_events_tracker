import factory

from models.events.location import Location

class LocationFactory(factory.Factory):
  class Meta:
    model = Location

  country_short = factory.Faker('country_code')
  country_long = factory.Faker('country')
  region = factory.Faker('country')
  city = factory.Faker('city')
  postal_code = factory.Faker('postcode')
  timezone = factory.Faker('timezone')
  latitude = factory.Faker('coordinate')
  longitude = factory.Faker('coordinate')
