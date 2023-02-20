from typing import Optional

from pydantic import BaseModel, Field

class WeatherBase(BaseModel):
  city: Optional[str] = Field(None, example="クリーニングを取りに行く")
  date: Optional[str] = Field(None, example="2023-02-12")
  weather: Optional[str] = Field(None, example="Cloudy")    
  temperature: int = Field(None, example=32)
  humidity: int = Field(None, example=12)


class Weather(WeatherBase):
    id: int
    class Config :
      orm_mode=True

class WeatherAdd(WeatherBase):
  pass

class WeatherAddResponse(WeatherAdd):
    id: int

    class Config:
        orm_mode = True