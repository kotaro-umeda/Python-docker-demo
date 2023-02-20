from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Weather(Base):
    __tablename__ = "weather_list"
    id = Column(Integer, primary_key=True,nullable=False)
    city = Column(String(1024),nullable=False)
    date = Column(String(1024),nullable=False)
    weather = Column(String(1024),nullable=False)
    temperature = Column(Integer,nullable=False)
    humidity = Column(Integer,nullable=False)

