from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import api.schemas.weather_info as weather_schema
import api.cruds.weather_info as weather_crud
from api.db import get_db

router = APIRouter()


@router.get("/weather",response_model=List[weather_schema.Weather])
async def list_weather(db:AsyncSession = Depends(get_db)):
    return await weather_crud.get_weather(db)


@router.post("/weather",response_model=weather_schema.WeatherAddResponse)
async def add_weather(weather_body:weather_schema.WeatherAdd,db:AsyncSession=Depends(get_db)):
  return await weather_crud.add_weather(db,weather_body)