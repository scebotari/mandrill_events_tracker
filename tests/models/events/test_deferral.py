from models.events.deferral import Deferral

class TestClick:
  def test_name(self):
    assert Deferral.name() == 'deferral'
