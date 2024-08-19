from wrappit.enums.mctype import MCType

class WorkingObject:
    def __init__(self, obj_type: MCType, name: str):
        self.type = obj_type
        self.name = name

    def to_dict(self):
        """
        Convert the WorkingObject to a dictionary for easy JSON serialization.
        """
        return {
            "type": self.type.value,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a WorkingObject from a dictionary (used during deserialization).
        """
        obj_type = MCType(data.get("type", MCType.UNKNOWN.value))
        name = data.get("name", "")
        return cls(obj_type, name)
