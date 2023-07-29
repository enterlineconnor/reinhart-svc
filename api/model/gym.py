"""Models regarding gym data."""

import qrcode
import pyqrcode
from pyqrcode import QRCode
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
            domain
        ) VALUES (
            ?,
            ?
        ) 
    """
    cursor = conn.cursor()
    cursor.execute(sql, new_gym.gym_name, new_gym.subdomain + ".reinhart.com")
    conn.commit()


def generate_gym_qr_code(gym_id: UUID, conn):
    sql = """
    SELECT domain FROM dbo.gym WHERE gym_id = ?
    """

    cursor = conn.cursor()
    row = cursor.execute(
        sql,
        gym_id,
    ).fetchone()

    if row:
        return pyqrcode.create(row.subdomain)
