"""Handle generic user CRUD operations server side calls."""

from fastapi import APIRouter, Depends
from ..model.user import get_all_users, UserResponse
from ..database.utils.uow import get_connection
router = APIRouter()


@router.get("")
async def get_all_user_info(conn = Depends(get_connection)) -> UserResponse | None:
    """GET all base data associated with the user."""
    return get_all_users(conn)
