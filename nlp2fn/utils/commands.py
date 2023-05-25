COMMANDS = {
    "add-source": "add_source",
    "run": "run",
    "reset": "reset",
    "delete": "delete_source",
    "exec": {
        "-m": "run_single_function"
    },
    "update": "update_source"
}

def map_command_to_function(args, mapping):
    function = None
    arguments = []

    current_map = mapping
    for arg in args:
        if isinstance(current_map, dict) and arg in current_map:
            current_map = current_map[arg]
        else:
            arguments.append(arg)

    if isinstance(current_map, str):
        function = current_map

    if function is None:
        raise ValueError("Function not found in the mapping")

    return function, arguments