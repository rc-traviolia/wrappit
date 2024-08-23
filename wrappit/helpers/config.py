import json
from pathlib import Path
from wrappit.enums.mctype import MCType
from wrappit.models.working_object import WorkingObject

CONFIG_FILE = Path("wrappit/config.json")

class ConfigHelper:
    def __init__(self):
        self.config = self.load_config()


    def get_working_root_directory(self):
        """
        Get the working root directory from the configuration.
        """
        return self.config["working_root_directory"]

    def get_behavior_pack_path(self):
        """
        Get the behavior pack path from the configuration.
        """
        return self.config["behavior_pack_path"]

    def get_resource_pack_path(self):
        """
        Get the resource pack path from the configuration.
        """
        return self.config["resource_pack_path"]

    def get_working_object(self):
        """
        Get the working object from the configuration.
        """
        return self.config["working_object"]

    def load_config(self):
        """
        Load the configuration from the config.json file, or return default values if the file doesn't exist.
        """
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                
                # Deserialize working_object if it exists
                if "working_object" in config:
                    config["working_object"] = WorkingObject.from_dict(config["working_object"])
                return config

        # Default config if config.json doesn't exist
        return {
            "working_root_directory": "",
            "behavior_pack_path": "",
            "resource_pack_path": "",
            "working_object": WorkingObject(MCType.UNKNOWN, "")
        }

    def save_config(self):
        """
        Save the current configuration to the config.json file.
        """
        config_to_save = self.config.copy()

        # Serialize the working_object
        if isinstance(config_to_save["working_object"], WorkingObject):
            config_to_save["working_object"] = config_to_save["working_object"].to_dict()

        with open(CONFIG_FILE, "w") as f:
            json.dump(config_to_save, f, indent=4)

    def set_working_root_directory(self, directory: str):
        """
        Set the working root directory in the configuration.
        """
        self.config["working_root_directory"] = directory
        self.save_config()

    def set_working_object(self, obj_type: MCType, name: str):
        """
        Set the working_object in the configuration.
        """
        self.config["working_object"] = WorkingObject(obj_type, name)
        self.save_config()
