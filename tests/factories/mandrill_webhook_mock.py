from datetime import datetime

import json
import uuid
import urllib.request
import hashlib
import hmac
import requests
import base64

class MandrillWebhookMock(object):
  def __init__(self, url, token):
    self.url = url
    self.token = token

  def post_events(self, events = None):
    events = events or MandrillWebhookMock.all()

    response = requests.post(
      self.url,
      json=events,
      headers={ 'X-Mandrill-Signature': self.signature() }
    )
    return response.text

  def signature(self):
    signature = hmac.new(
      bytes(self.token, 'utf-8'),
      bytes(self.url, 'utf-8'),
      hashlib.sha1
    )
    return base64.b64encode(signature.digest())

  @staticmethod
  def all():
    return [
      MandrillWebhookMock.click(),
      MandrillWebhookMock.open(),
      MandrillWebhookMock.bounce('hard_bounce'),
      MandrillWebhookMock.bounce('soft_bounce'),
      MandrillWebhookMock.generic_event('send'),
      MandrillWebhookMock.generic_event('deferral'),
      MandrillWebhookMock.generic_event('spam'),
      MandrillWebhookMock.generic_event('unsub'),
      MandrillWebhookMock.generic_event('reject')
    ]
  
  @staticmethod
  def common_payload():
    msg_id = str(uuid.uuid4())
    return {
      'ts': int(datetime.utcnow().timestamp()),
      '_id': msg_id,
      'msg': {
        '_id': msg_id,
        # Simulate message was sent 1 hour ago
        'ts': int(datetime.utcnow().timestamp()) - 3600,
        'email': 'recipient@example.com',
        'sender': 'no-reply@example.com',
        'subject': 'Test message'
      }
    }
  
  @staticmethod
  def common_recipient_payload():
    return {
      **MandrillWebhookMock.common_payload(),
      'ip': '8.8.8.8',
      'user_agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
      'location': {
        'country_short': 'MD',
        'country_long': 'Moldova, Rep. of',
        'region': 'Chisinau',
        'city': 'Chisinau',
        'postal_code': '2043',
        'timezone': 'GMT+3',
        'latitude': '47.010530',
        'longitude': '28.863820'
      },
      'user_agent_parsed': {
        'mobile': False,
        'os_company': 'Google',
        'os_company_url': 'https://google.com/',
        'os_family': 'linux',
        'os_name': 'Ubuntu',
        'os_url': 'https://ubuntu.com/',
        'type': 'browser',
        'ua_company': 'Google',
        'ua_company_url': 'https://google.com/',
        'ua_family': 'Chrome',
        'ua_name': 'Mozilla/5.0',
        'ua_url': 'https://developer.mozilla.org/',
        'ua_version': '89'
      }
    }

  @staticmethod
  def open():
    return {
      'event': 'open',
      **MandrillWebhookMock.common_recipient_payload()
    }
  
  @staticmethod
  def click():
    return {
      'url': 'https://example.com',
      'event': 'click',
      **MandrillWebhookMock.common_recipient_payload()
    }

  @staticmethod
  def generic_event(event):
    return {
      'event': event,
      **MandrillWebhookMock.common_payload()
    }

  @staticmethod
  def bounce(event):
    payload = {
      'event': event,
      **MandrillWebhookMock.common_payload()
    }

    payload['msg']['diag'] = 500
    payload['msg']['bounce_description'] = 'bad_mailbox'

    return payload

if __name__ == '__main__':
  MandrillWebhookMock('http://localhost:8000/mandrill/webhook', 'test-api-key').post_events()
