"""Handle generic client CRUD operations server side calls."""

from uuid import UUID
from fastapi import APIRouter, Depends
from ..model.client import (
    ClientResponse,
    NewClientPayload,
    get_all_clients,
    create_new_client,
)
from ..database.utils.uow import get_connection

router = APIRouter()


@router.get("")
async def get_all_client_info(conn=Depends(get_connection)) -> ClientResponse | None:
    """GET all base data associated with the client."""
    return get_all_clients(conn)


@router.post("/{gym_id}")
async def create_client(
    new_client: NewClientPayload, gym_id: UUID, conn=Depends(get_connection)
):
    """Create new client for gym"""
    create_new_client(new_client, gym_id, conn)
    return {"message": "success"}
