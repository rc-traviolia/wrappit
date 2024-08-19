import os
import typer
from wrappit.helpers.config import ConfigHelper
from wrappit.helpers.directory_traversal import check_for_pack_paths
from wrappit.commands.utility import print_directory_structure

app = typer.Typer()

@app.command()
def utility():
    print_directory_structure()

@app.command()
def init():
    """
    Initialize the project by setting the working_root_directory to the current directory,
    creating a .mcdev folder, and saving the configuration. Print a confirmation message with the path.
    """
    # # Get the current directory
    # current_directory = os.getcwd()

    # # Create the .mcdev directory
    # mcdev_directory = os.path.join(current_directory, ".mcdev")
    # os.makedirs(mcdev_directory, exist_ok=True)

    # # Create a ConfigHelper instance
    # config_helper = ConfigHelper()

    # # Set the working root directory in the config and save
    # config_helper.set_working_root_directory(current_directory)

    # # Save the configuration in the .mcdev folder
    # config_helper.save_config(os.path.join(mcdev_directory, "config.json"))

    # # Save the updated configuration and report success
    # typer.echo(f"mcdev initialized at: {current_directory}")
    # typer.echo(check_for_pack_paths(current_directory))

@app.command()
def show():
    """
    Show the current working_root_directory from the config.
    """
    # Create a ConfigHelper instance
    config_helper = ConfigHelper()

    # Retrieve the working root directory
    working_root_directory = config_helper.config.get("working_root_directory", "Not set")

    # Display the working root directory
    typer.echo(f"Working Root Directory: {working_root_directory}")

if __name__ == "__main__":
    app(prog_name="mcdev")
