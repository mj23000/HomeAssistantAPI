"""File for models used in responses from entity registry."""

from enum import Enum
from typing import Any, Dict, List, Optional

from .base import BaseModel


class RegistryEntryDisabler(Enum):
    """What disabled a registry entry."""

    CONFIG_ENTRY = "config_entry"
    DEVICE = "device"
    HASS = "hass"
    INTEGRATION = "integration"
    USER = "user"


class EntityCategory(Enum):
    """Category of an entity.

    An entity with a category will:
    - Not be exposed to cloud, Alexa, or Google Assistant components
    - Not be included in indirect service calls to devices or areas
    """

    CONFIG = "config"
    DIAGNOSTIC = "diagnostic"


class RegistryEntryHider(Enum):
    """What hid a registry entry."""

    INTEGRATION = "integration"
    USER = "user"


class EntityConfigEntry(BaseModel):
    """An entity configuration entry. This is the model that Home Assistant returns, but not what is used internally."""

    area_id: Optional[str]
    categories: Dict[str, str]
    config_entry_id: Optional[str]
    config_subentry_id: Optional[str]
    created_at: float
    device_id: Optional[str]
    disabled_by: Optional[RegistryEntryDisabler]
    entity_category: Optional[EntityCategory]
    entity_id: str
    has_entity_name: bool
    hidden_by: Optional[RegistryEntryHider]
    icon: Optional[str]
    id: str
    labels: List[str]
    modified_at: float
    name: Optional[str]
    options: Dict[str, Dict[str, Any]]
    original_name: Optional[str]
    platform: str
    translation_key: Optional[str]
    unique_id: str
