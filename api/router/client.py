"""Handle generic client CRUD operations server side calls."""

from fastapi import APIRouter, Depends
from ..model.client import get_all_clients, ClientResponse
from ..database.utils.uow import get_connection

router = APIRouter()


@router.get("")
async def get_all_client_info(conn=Depends(get_connection)) -> ClientResponse | None:
    """GET all base data associated with the client."""
    return get_all_clients(conn)
