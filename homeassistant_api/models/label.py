"""Module for Label data models"""

from enum import Enum
from typing import Optional

from homeassistant_api.utils import JSONType

from .base import BaseModel


class LabelColors(Enum):
    PRIMARY = "primary"
    ACCENT = "accent"
    DISABLED = "disabled"
    RED = "red"
    PINK = "pink"
    PURPLE = "purple"
    DEEP_PURPLE = "deep-purple"
    INDIGO = "indigo"
    BLUE = "blue"
    LIGHT_BLUE = "light-blue"
    CYAN = "cyan"
    TEAL = "teal"
    GREEN = "green"
    LIGHT_GREEN = "light-green"
    LIME = "lime"
    YELLOW = "yellow"
    AMBER = "amber"
    ORANGE = "orange"
    DEEP_ORANGE = "deep-orange"
    BROWN = "brown"
    LIGHT_GREY = "light-grey"
    GREY = "grey"
    DARK_GREY = "dark-grey"
    BLUE_GREY = "blue-grey"
    BLACK = "black"
    WHITE = "white"


class Label(BaseModel):
    """Represents label entries inside of Home Assistant label registry"""

    color: Optional[LabelColors]
    created_at: float
    description: Optional[str]
    icon: Optional[str]
    label_id: str
    modified_at: float
    name: str

    @classmethod
    def from_json(cls, json: dict[str, JSONType]) -> "Label":
        """Constructs State model from json data"""
        return cls.model_validate(json)
