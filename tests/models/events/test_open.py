from models.events.open import Open

class TestOpen:
  def test_name(self):
    assert Open.name() == 'open'
