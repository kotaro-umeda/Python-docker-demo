from sqlalchemy.ext.asyncio import AsyncSession

import api.models.weather_info as weather_model
import api.schemas.weather_info as weather_schema
from typing import List,Tuple
from sqlalchemy import select
from sqlalchemy.engine import Result


async def add_weather(
    db: AsyncSession, weather_add: weather_schema.WeatherAdd
) -> weather_model.Weather:
    weather = weather_model.Weather(**weather_add.dict())
    db.add(weather)
    await db.commit()
    await db.refresh(weather)
    return weather

async def get_weather(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                weather_model.Weather.id,
                weather_model.Weather.city,
                weather_model.Weather.date,
                weather_model.Weather.humidity,
                weather_model.Weather.temperature,
                weather_model.Weather.weather,
            )
        )
    )
    return result.all()