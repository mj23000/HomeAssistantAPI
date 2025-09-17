"""File for models used in responses from entity registry."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import Field

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


class SimplifiedEntityConfigEntry(BaseModel):
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


class DisplayConfigEntry(BaseModel):
    """An entity display entry. This is the model that Home Assistant returns, but not what is used internally."""

    area_id: Optional[str] = Field(alias="ai", default=None)
    device_id: Optional[str] = Field(alias="di", default=None)
    entity_category: Optional[int] = Field(alias="ec", default=None)
    entity_id: str = Field(alias="ei")
    entity_name: Optional[str] = Field(alias="en", default=None)
    has_name: Optional[bool] = Field(alias="hn", default=None)
    icon: Optional[str] = Field(alias="ic", default=None)
    labels: Optional[List[str]] = Field(alias="lb", default=None)
    platform: str = Field(alias="pl")
    translation_key: Optional[str] = Field(alias="tk", default=None)


class DisplayConfigEntries(BaseModel):
    """Entity display entries. This is the model that Home Assistant returns, but not what is used internally."""

    entity_categories: Dict[str, EntityCategory]
    entities: List[DisplayConfigEntry]


class EntityConfigEntry(SimplifiedEntityConfigEntry):
    """An entity configuration entry. This is the model that Home Assistant returns, but not what is used internally."""

    # TODO: Ensure valid default values
    previous_unique_id: Optional[str] = None
    aliases: set[str] = set()
    capabilities: Optional[Dict[str, str]]
    created_at: datetime
    device_class: Optional[str]
    domain: Optional[str] = None
    modified_at: datetime
    original_device_class: Optional[str]
    original_icon: Optional[str]
    supported_features: Optional[int] = None
    unit_of_measurement: Optional[str] = None
