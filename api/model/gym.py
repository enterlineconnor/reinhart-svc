"""Models regarding gym data."""

from uuid import UUID
from pydantic import BaseModel


class GymPayload(BaseModel):
    gym_name: str
    subdomain: str


def create_gym(new_gym: GymPayload, conn):
    """Get all user data"""

    sql = """
        INSERT INTO dbo.gym (
            gym_name,
            subdomain
        ) VALUES (
            ?,
            ?
        ) 
    """
    cursor = conn.cursor()
    cursor.execute(sql, new_gym.gym_name, new_gym.subdomain)
    conn.commit()
