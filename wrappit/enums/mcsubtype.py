# mcdev/mctype.py
from enum import Enum

class MCSubType(str, Enum):
    Entity = "behavior"
    Item = "resource"
    UNKNOWN = "unknown"
