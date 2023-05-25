import json
import os
from nlp2fn.sourcehandler.git.repo import Repo

def download_github_source(source, source_directory):
    """
    Clones a git repository to the specified source directory if it doesn't already exist.
    :param source: The URL of the git repository.
    :param source_directory: The directory to store the cloned repository.
    :return: The name of the cloned repository.
    """
    repo_name = source.split("/")[-1]
    download_path = os.path.join(source_directory, repo_name)
    repo = Repo(source_directory)

    if os.path.exists(download_path):
        print(f"The event source '{repo_name}' already exists. No need to download.")
        repo.pull()
        return repo_name

    # Try making the directory if it doesn't exist.
    try:
        os.makedirs(download_path)
    except Exception as e:
        pass

    repo = Repo(source_directory)
    clone_output = repo.clone(source)
    if "fatal" in clone_output.lower():
        raise ValueError(f"Failed to clone the repository: {source}")
    else:
        print(f"The repository '{repo_name}' has been cloned successfully.")
        return repo_name

def get_statement_from_file(filepath, function_mapping):
    """
    Extracts statements from a file and maps them to the corresponding function or filepath.
    :param filepath: The path to the file.
    :param function_mapping: The mapping of statements to functions or filepaths.
    :return: The updated function_mapping.
    """
    event_name = filepath.split("/")[-2]
    file = filepath.split("/")[-1]
    lines = open(filepath).read().splitlines()
    for line in lines:
        if "STATEMENT" in line:
            try:
                statement = line.split("=")[1]
                if "]" in statement and "[" in statement:
                    data = json.loads(statement)
                    for key in data:
                        function_mapping[key] = event_name + "." + file.split(".")[0]
                else:
                    if "'" in statement:
                        statement = statement.split("'")[1]
                    else:
                        statement = statement.split('"')[1]

                    function_mapping[statement] = filepath
            except Exception as e:
                pass

    return function_mapping

def fetch_statement(directory):
    """
    Fetches statements from all Python files within a directory and its subdirectories.
    :param directory: The directory to search for Python files.
    :return: The mapping of statements to functions or filepaths.
    """
    function_mapping = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                function_mapping = get_statement_from_file(
                    os.path.join(directory, file),
                    function_mapping
                )
    return function_mapping

def select_from_sources(source_options):
    print("Available sources:")
    for i, option in enumerate(source_options, 1):
        print(f"{i}. {option}")

    while True:
        user_input = input("Enter the number or name of the source: ")

        if user_input.isdigit():
            index = int(user_input) - 1
            if index >= 0 and index < len(source_options):
                selected_source = source_options[index]
                break
        else:
            if user_input in source_options:
                selected_source = user_input
                break

        print("Invalid input. Please enter a valid number or name.")

    return selected_source



def delete_source_from_conf(data, source_name, output_dir):
    # Check if the source exists in the dictionary
    if source_name in data["sources"]:
        source_path = data["sources"][source_name]

        # If the source value starts with 'https://github.com'
        if source_path.startswith("https://github.com"):
            source_output_dir = os.path.join(output_dir, source_path.split("/")[-1])
            os.system(f"rm -rf {source_output_dir}")
        else:
            source_output_dir = source_path

        # Generate the path to delete from statements
        delete_path = os.path.normpath(source_output_dir)

        # Remove the source from the dictionary
        del data["sources"][source_name]

        # Remove statements that start with the generated path
        data["statements"] = {statement: path for statement, path in data["statements"].items() if not path.startswith(delete_path)}

    return data
