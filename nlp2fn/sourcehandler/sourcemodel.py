import configparser
import os

from nlp2fn.sourcehandler.helper import *

CONFIG_FILE_NAME = "nlp2fn.source.conf"
EVENT_CONF_FILE = "nlp2fn.events.json"

class SourceModel:
    def __init__(self, directory="~/nlp2fn"):
        self.directory = os.path.expanduser(directory)
        self.source_directory = os.path.join(self.directory, "sources")
        self.file = os.path.join(self.directory, CONFIG_FILE_NAME)

        self.init_model()

    def init_model(self):
        # Create the necessary directories and files if they don't exist
        os.makedirs(self.directory, exist_ok=True)
        os.makedirs(self.source_directory, exist_ok=True)
        if not os.path.exists(self.file):
            open(self.file, "w").write("[sources]\n[statements]\n")
        return True

    def get_section(self, section_name):
        # Read the config file and return the specified section as a dictionary
        config = configparser.ConfigParser()
        config.read(self.file)
        resp = {}
        if section_name in config:
            resp = dict(config[section_name])

        return resp

    def get_statements(self):
        # Get the statements section as a dictionary
        return self.get_section("statements")

    def get_sources(self):
        # Get the sources section as a dictionary
        return self.get_section("sources")

    def get(self):
        # Get the combined statements and sources as a dictionary
        return {
            "statements": self.get_statements(),
            "sources": self.get_sources()
        }

    def save(self, data):
        # Save the statements and sources dictionaries to the config file
        config = configparser.ConfigParser()

        # Iterate over sources and add them to the config object
        config["sources"] = data["sources"]

        # Iterate over statements and add them to the config object
        config["statements"] = data["statements"]

        # Write the configuration to a file
        with open(self.file, 'w') as file:
            config.write(file)

    def add(self, source):
        """
        Add a new source to the source file.
        """

        if source.startswith("https://github.com/"):
            # If the source is a remote GitHub repository, download it to the source directory
            path = os.path.join(self.source_directory, source.split("/")[-1])
            download_github_source(source, self.source_directory)
        elif os.path.isdir(source):
            # If the source is a local directory, use it as the path
            path = source
        else:
            # Invalid source input
            raise ValueError(f"Invalid source {source}. Source must be a GitHub repository URL or a valid local directory path.")

        # Check if nlp2fn.events.json exists and grab the events directory from it
        events_sub_dir = ""
        if os.path.exists(os.path.join(path, EVENT_CONF_FILE)):
            try:
                events_sub_dir = json.loads(open(os.path.join(path, "nlp2fn.events.json")).read())["events"]
            except Exception as e:
                pass

        source_name = path.split("/")[-1]
        statements = fetch_statement(os.path.join(path, events_sub_dir))

        try:
            requirements_filepath = os.path.join(path, "requirements.txt")
            if os.path.exists(requirements_filepath):
                os.system(f"pip install -r {requirements_filepath}")
        except Exception as e:
            pass

        info = self.get()
        info["statements"].update(statements)
        if source.startswith("https://github.com/"):
            info["sources"][source_name] = source
        else:
            info["sources"][source_name] = path
        self.save(info)

    def match(self, statement):
        """
        The function takes a statement matches with the present statement from source
        return either None or fn_file_path, arguments.
        :param statement: analyse data from {csv_file_path}
        :return: either None or fn_file_path, arguments.
        """
        mappings = self.get_statements()

        for pattern, function_name in mappings.items():
            pattern_parts = pattern.lower().split()
            statement_parts = statement.lower().split()

            if len(pattern_parts) != len(statement_parts):
                continue

            params = {}
            match = True
            for pattern_part, statement_part in zip(pattern_parts, statement_parts):
                if pattern_part.startswith("{") and pattern_part.endswith("}"):
                    param_name = pattern_part[1:-1]
                    params[param_name] = statement_part
                elif pattern_part != statement_part:
                    match = False
                    break

            if match:
                return function_name, params
        return None, None

    def remove(self, source_name=None):
        # if source name is not provided show user option of all source and allow him to select.
        if source_name == None:
            config = configparser.ConfigParser()
            config.read(self.file)

            sources = config["sources"]
            source_options = list(sources.keys())
            source_name = select_from_sources(source_options)

        sourceInfo = self.get()
        sourceInfo = delete_source_from_conf(sourceInfo, source_name, self.source_directory)
        self.save(sourceInfo)

        return True

    def reset(self):
        # Reset the source file and source directory
        os.system(f"rm -rf {self.file}")
        os.system(f"rm -rf {self.source_directory}")
        print("All sources have been removed successfully.")
