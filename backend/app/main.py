from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import stations

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://subteba.netlify.app",
]

# Add CORSMiddleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows these origins
    allow_credentials=True,  # Allow credentials (cookies, authorization headers)
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

prefix = "/api"
app.include_router(stations.router, prefix=prefix, tags=["stations"])
