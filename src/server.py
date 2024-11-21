from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config.security.cors import methods, origins
from .routers import evaluation_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=["*"],
)

app.include_router(evaluation_router)
