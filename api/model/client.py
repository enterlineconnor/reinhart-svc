"""Models regarding client data."""

from uuid import UUID
from pydantic import BaseModel


class ClientResponse(BaseModel):
    """Client data for response operations"""

    client_id: UUID
    first_name: str
    last_name: str
    phone: str
    email: str


class NewClientPayload(BaseModel):
    """New client data."""

    first_name: str
    last_name: str
    phone: str
    email: str


def get_all_clients(conn) -> ClientResponse | None:
    """Get all client data."""

    sql = """
        SELECT
            client_id,
            first_name,
            last_name,
            phone,
            email
        FROM dbo.client  
    """
    cursor = conn.cursor()
    row = cursor.execute(sql).fetchone()
    if row:
        return ClientResponse(
            client_id=row.client_id,
            first_name=row.first_name,
            last_name=row.last_name,
            phone=row.phone,
            email=row.email,
        )
    return None


def create_new_client(new_client: NewClientPayload, gym_id: UUID, conn):
    """Create new client associated with gym."""
    sql = """
        INSERT INTO dbo.client (
            gym_id,
            first_name,
            last_name,
            phone,
            email
        ) VALUES (
            ?,
            ?,
            ?,
            ?,
            ?
        )
    """
    cursor = conn.cursor()
    cursor.execute(
        sql,
        gym_id,
        new_client.first_name,
        new_client.last_name,
        new_client.phone,
        new_client.email,
    )
    cursor.commit()
