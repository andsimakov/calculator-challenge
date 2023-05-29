from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.constants import PROJECT_NAME, PROJECT_VERSION
from api.v1.api import api_router


app = FastAPI(title=PROJECT_NAME, description=f"{PROJECT_NAME}'s API v{PROJECT_VERSION}", version=PROJECT_VERSION)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

app.include_router(api_router, prefix="/api/v1")
