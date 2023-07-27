"""Requests related to gym based processes"""

from fastapi import APIRouter, Depends
from ..model.gym import create_gym
from ..database.utils.uow import get_connection
router = APIRouter()


@router.post("")
async def create_new_gym(conn = Depends(get_connection)):
    """GET all base data associated with the user."""
    create_gym(conn)
    return {"message": "success"}
