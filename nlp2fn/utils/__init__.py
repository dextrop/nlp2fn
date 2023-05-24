import os
from nlp2fn.utils.colorpriniting import error

# Set up the location of the configuration file.
TOKEN_PATH = os.path.expanduser("~/.nlp2fn.conf.json")


def get_py_fnc_dir():
    """
    This function reads the configuration file specified by TOKEN_PATH.
    It expects each line of the file to represent a location (either a URL or a filesystem path).
    It then checks if the filesystem paths exist, and returns all locations.
    """

    # Ensure the configuration file exists. If not, create an empty one.
    if not os.path.isfile(TOKEN_PATH):
        open(TOKEN_PATH, 'a').close()

    with open(TOKEN_PATH, 'r') as file:
        content = file.read().splitlines()

    directories = []

    for key in content:
        # If the key doesn't start with "http", assume it's a filesystem path.
        if not key.startswith("http"):
            # Check if the path exists, if so, add it to the list.
            if os.path.exists(key):
                directories.append(key)
        else:  # The key is a URL.
            directories.append(key)

    return directories

def update_py_fnc_dir(directory):
    """
    Adds a new directory to the configuration file specified by TOKEN_PATH.
    If the directory is a local filesystem path, checks if it exists before adding.
    If the directory is a URL, it is added without any existence check.

    Args:
        directory (str): The directory to add. Can be a local filesystem path or a URL.
    """

    # If the directory doesn't start with "http", assume it's a filesystem path.
    if not os.path.exists(directory):
        raise ValueError(f"Directory {directory} does not exits")

    lines = open(TOKEN_PATH).read().splitlines()
    if directory in lines:
        error("Source Already Exits")
        return

    with open(TOKEN_PATH, 'a') as file:
        file.write(f"{directory}\n")

    return get_py_fnc_dir()

def delete_py_fnc_dir_info():
    os.remove(TOKEN_PATH)


