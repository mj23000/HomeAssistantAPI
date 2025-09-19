"""Models for logger."""

from .base import BaseModel

class LoggerInfo(BaseModel):
    """Information about a domain's logger."""

    domain: str
    level: int
