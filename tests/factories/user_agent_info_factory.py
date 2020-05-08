import factory

from models.events.user_agent_info import UserAgentInfo

class UserAgentInfoFactory(factory.Factory):
  class Meta:
    model = UserAgentInfo

  mobile = False
  os_company = 'Google inc.'
  os_company_url = 'https://google.com'
  os_family = 'Linux'
  os_icon = None
  os_name = 'Ubuntu 18.04'
  os_url = 'https://ubuntu.org'
  type = 'browser'
  ua_company = 'Google inc.'
  ua_company_url = 'https://google.com'
  ua_family = 'Chrome'
  ua_icon = None
  ua_name = factory.Faker('linux_platform_token')
  ua_url = factory.Faker('chrome')
  ua_version = '80'
