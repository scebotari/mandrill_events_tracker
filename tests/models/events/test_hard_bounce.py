from models.events.hard_bounce import HardBounce

class TestClick:
  def test_name(self):
    assert HardBounce.name() == 'hard_bounce'
