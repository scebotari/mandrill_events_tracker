from models.events.reject import Reject

class TestOpen:
  def test_name(self):
    assert Reject.name() == 'reject'
