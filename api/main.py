"""Centralized location for prefix declaration for each route."""

from fastapi import FastAPI
from .router import client, gym


app = FastAPI(
    title="Reinhart API",
    description="Access to data that supports Reinhart frontend application",
    version=0.1,
)

app.include_router(
    gym.router,
    prefix="/gym",
)

app.include_router(
    client.router,
    prefix="/client",
)
