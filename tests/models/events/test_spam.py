from models.events.spam import Spam

class TestOpen:
  def test_name(self):
    assert Spam.name() == 'spam'
