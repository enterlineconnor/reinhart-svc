"""Requests related to gym based processes"""

from uuid import UUID
from fastapi import APIRouter, Depends
from starlette.responses import StreamingResponse
from ..model.gym import GymPayload, create_gym, generate_gym_qr_code
from ..database.utils.uow import get_connection

router = APIRouter()


@router.post("")
async def create_new_gym(new_gym: GymPayload, conn=Depends(get_connection)):
    """Create new gym."""
    create_gym(new_gym, conn)
    return {"message": "success"}


@router.get("/{gym_id}/qrcode")
def get_gym_qr_code(gym_id: UUID, conn=Depends(get_connection)):
    """Return qrcode based on gym id param for client sign up."""
    buf = generate_gym_qr_code(gym_id, conn)
    return StreamingResponse(buf, media_type="image/jpeg")
