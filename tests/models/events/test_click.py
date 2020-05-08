from models.events.click import Click

class TestClick:
  def test_name(self):
    assert Click.name() == 'click'
