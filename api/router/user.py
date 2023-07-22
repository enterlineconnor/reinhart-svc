"""Handle generic user CRUD operations server side calls."""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    """Generic Message."""
    return {"message": "Hello World"}
