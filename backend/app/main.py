from fastapi import FastAPI
from app.routers import stations

app = FastAPI()

prefix = "/api"
app.include_router(stations.router, prefix=prefix, tags=["stations"])
