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
