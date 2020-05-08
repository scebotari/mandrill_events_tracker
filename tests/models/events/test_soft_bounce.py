from models.events.soft_bounce import SoftBounce

class TestClick:
  def test_name(self):
    assert SoftBounce.name() == 'soft_bounce'
