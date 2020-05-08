from models.events.send import Send

class TestOpen:
  def test_name(self):
    assert Send.name() == 'send'
