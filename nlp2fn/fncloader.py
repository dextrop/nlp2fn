import os, re
import importlib.util
from nlp2fn.utils.colorpriniting import *

class FunctionLoader():
    def set_source(self, sources=None):
        if sources is None:
            sources = []
        self.sources = sources
        self.func_map = {}
        return self.setup

    def list_all_files_from_dir(self, PATH):
        result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(PATH) for f in filenames if
                  os.path.splitext(f)[1] == '.py' and "__init__.py" not in f]
        return result

    def convert_to_dict(self, statement):
        parts = re.split(r'\{.*?\}', statement)
        variables = re.findall(r'\{(.+?)\}', statement)
        pattern = '(.+)'.join(parts)
        return pattern, variables

    def parse_statement(self, parseStatment, statement):
        match = re.match(parseStatment, statement)
        if match:
            resp = match.groups()
            return list(resp)
        return None

    def get_statement(self, py_fnc_filepath):
        '''
        Load all functions from a directry, check for statement and execute function,
        throw error if function or statement is not found.
        :param py_fnc_filepath: Directory path of any python statement.
        :return: statement, execute function object.
        '''
        file_content = open(py_fnc_filepath).read()
        try:
            if "statement" in file_content:
                statement = file_content.split("statement")[1].split("=")[1].split('"')[1]
        except Exception as e:
            raise ValueError(f"There is not statement present in {py_fnc_filepath}")
        spec = importlib.util.spec_from_file_location(py_fnc_filepath.split("/")[-1].split(".")[0], py_fnc_filepath)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        try:
            return statement, foo.execute
        except Exception as e:
            raise ValueError(f"There is no execute function found in {py_fnc_filepath}")

    @property
    def setup(self):
        for dir in self.sources:
            for key in self.list_all_files_from_dir(dir):
                statement, fnc = self.get_statement(key)
                pattern, variables = self.convert_to_dict(statement)
                self.func_map[pattern] = {"variables": variables, "fnc": fnc, "statement": statement}

        return None

    def execute(self, command):
        for key in self.func_map:
            result = self.parse_statement(key.lower(), command.lower())
            if result != None:
                success ("Statement: " + command)
                success ("Executing: " + self.func_map[key]["statement"])
                self.func_map[key]["fnc"](result)

        return None