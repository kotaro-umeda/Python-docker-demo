from fastapi import FastAPI

from api.routers import weather_info

app = FastAPI()
origins = [
    "http://localhost:3000","https://react-python-demo.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(weather_info.router)
