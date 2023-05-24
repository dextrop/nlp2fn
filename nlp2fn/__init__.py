import sys, os
from nlp2fn.utils.commands import COMMANDS, map_command_to_function
from nlp2fn.fncloader import FunctionLoader
from nlp2fn.utils import update_py_fnc_dir, get_py_fnc_dir, delete_py_fnc_dir_info
from nlp2fn.utils.colorpriniting import error
from nlp2fn.clonefromgit import GitEvents

fnLoader = FunctionLoader()

def reset_src_dir(args):
    delete_py_fnc_dir_info()

def set_github_source(args):
    if len(args) < 1:
        raise ValueError("Missing Githib link.")
    GitEvents(args[0])

def set_source_dir(args):
    if len(args) < 1:
        raise ValueError("Missing directory link.")

    directory = args[0]
    if not os.path.exists(directory) and directory[:4] != "http":
        raise ValueError(f"Directory {directory} does not exits")

    if os.path.expanduser("~/") in directory:
        update_py_fnc_dir(directory)
    else:
        update_py_fnc_dir(os.path.join(os.getcwd(), directory))

def run(args):
    directories = get_py_fnc_dir()
    if len(directories) < 1:
        raise ValueError("Missing source directory")

    fnLoader.set_source(directories)

    while(True):
        print ("How can I help ?")
        statement = input(">> ")
        fnLoader.execute(
            statement
        )


def run_command(args):
    directories = get_py_fnc_dir()
    if len(directories) < 1:
        raise ValueError("Missing source directory")

    fnLoader.set_source(directories)
    fnLoader.execute(
        args[0]
    )

def execute():
    try:
        fn_name, args = map_command_to_function(sys.argv[1:], COMMANDS)
        if fn_name == "set_local_source":
            return set_source_dir(args)
        elif fn_name == "set_github_source":
            return set_github_source(args)
        elif fn_name == "run":
            return run(args)
        elif fn_name == "run_single_function":
            return run_command(args)
        elif fn_name == "reset":
            return reset_src_dir(args)

        raise ValueError("Invalid Command")
    except Exception as e:
        error(str(e))
