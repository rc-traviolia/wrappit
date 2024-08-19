from enum import Enum

class MCType(str, Enum):
    Entity = "behavior"
    Item = "resource"
    UNKNOWN = "unknown"
