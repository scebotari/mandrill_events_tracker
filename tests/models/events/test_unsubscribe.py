from models.events.unsubscribe import Unsubscribe

class TestOpen:
  def test_name(self):
    assert Unsubscribe.name() == 'unsubscribe'
