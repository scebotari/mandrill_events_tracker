from pydantic import BaseModel

class UserAgentInfo(BaseModel):
  mobile: bool = None
  os_company: str = None
  os_company_url: str = None
  os_family: str = None
  os_icon: str = None
  os_name: str = None
  os_url: str = None
  type: str = None
  ua_company: str = None
  ua_company_url: str = None
  ua_family: str = None
  ua_icon: str = None
  ua_name: str = None
  ua_url: str = None
  ua_version: str = None
