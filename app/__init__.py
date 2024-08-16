from fastapi import FastAPI
from app.api import router
from app import db
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
add_pagination(app)
