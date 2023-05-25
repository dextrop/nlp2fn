import importlib.util

def run_function_from_file(file_path, function_name, params):
    try:
        # Create a module specification from the file path
        spec = importlib.util.spec_from_file_location("custom_module", file_path)

        # Create a module from the specification
        module = importlib.util.module_from_spec(spec)

        # Load the module
        spec.loader.exec_module(module)

        # Get the function from the module
        function = getattr(module, function_name)

        # Run the function with the provided arguments
        result = function(params)

        return result
    except (ImportError, AttributeError) as e:
        print(f"Failed to import or run function from file: {e}")