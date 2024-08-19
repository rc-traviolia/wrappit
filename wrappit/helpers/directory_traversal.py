import os

import os

def check_for_pack_paths(working_root_directory : str):
    """
    This function checks the current working_root_directory for folders that match
    resource and behavior pack patterns, and returns lists of possible pack folders.
    """
    #working_root_directory = config["working_root_directory"]

    # Lists to store possible resource and behavior pack folders
    possible_resource_packs = []
    possible_behavior_packs = []

    # Iterate through the directories in working_root_directory
    for folder_name in os.listdir(working_root_directory):
        folder_path = os.path.join(working_root_directory, folder_name)
        
        if os.path.isdir(folder_path):
            # Check for resource packs (ends with _RP, -RP, or contains 'Resource')
            if folder_name.lower().endswith(('_rp', '-rp')) or 'resource' in folder_name.lower():
                possible_resource_packs.append(folder_name)
            
            # Check for behavior packs (ends with _BP, -BP, or contains 'Behavior')
            if folder_name.lower().endswith(('_bp', '-bp')) or 'behavior' in folder_name.lower():
                possible_behavior_packs.append(folder_name)

    # Set default paths and create directories if not existing
    #config["behavior_pack_path"] = os.path.join(working_root_directory, "behavior_packs")
    #config["resource_pack_path"] = os.path.join(working_root_directory, "resource_packs")

    #os.makedirs(config["behavior_pack_path"], exist_ok=True)
    #os.makedirs(config["resource_pack_path"], exist_ok=True)

    # Return the two lists of possible resource and behavior pack folders
    return possible_resource_packs, possible_behavior_packs

