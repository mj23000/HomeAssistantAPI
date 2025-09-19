"""Models for logger."""

from enum import Enum

from .base import BaseModel


class LoggerInfo(BaseModel):
    """Information about a domain's logger."""

    domain: str
    level: int


class LogPersistence(str, Enum):
    """Log persistence."""

    NONE = "none"
    ONCE = "once"
    PERMANENT = "permanent"
