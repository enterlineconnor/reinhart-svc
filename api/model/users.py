"""Models regarding user data."""

from uuid import UUID
from pydantic import BaseModel



class UserResponse(BaseModel):
    """User data for response operations"""
    user_id: UUID
    first_name: str
    last_name: str
    phone: str
    email: str


def get_all_users(conn) -> UserResponse | None:
    """Get all user data"""

    sql = """
        SELECT
            user_id,
            first_name,
            last_name,
            phone,
            email
        FROM dbo.user_info  
    """
    cursor = conn.cursor()
    row = cursor.execute(sql).fetchone()
    if row:
        return UserResponse(
            user_id=row.user_id,
            first_name=row.first_name,
            last_name=row.last_name,
            phone=row.phone,
            email=row.email
        )
    return None
