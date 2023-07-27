"""Generate connection for DB interaction."""
import logging
import pyodbc
from ...database import config

logger = logging.getLogger(__name__)


def _get_connection_string():
    """Connection string for database."""
    return (f"Driver={config.DRIVER};"
                f"Server={config.SERVER};"
                f"UID={config.UID};"
                f"PWD={config.PWD};"
                f"Database={config.DATABASE};"
                "TrustServerCertificate=yes;")


def get_connection():
    """Return db connection object."""
    return pyodbc.connect(_get_connection_string())
