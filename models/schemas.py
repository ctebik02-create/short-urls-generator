from pydantic import BaseModel, HttpUrl, ConfigDict

class UrlInput(BaseModel):
    url: HttpUrl

class UrlOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    original_url: HttpUrl
    short_code: str

class StatisticOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    original_url: HttpUrl
    clicks: int
    short_code: str
    condition: bool
