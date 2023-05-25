import sys
from nlp2fn.utils.commands import COMMANDS, map_command_to_function
from nlp2fn.utils.colorpriniting import error
from nlp2fn.interface import NLP2FnInterface

def execute():
    interface = NLP2FnInterface()
    try:
        fn_name, args = map_command_to_function(sys.argv[1:], COMMANDS)

        if fn_name == "run":
            return interface.run()

        elif fn_name == "run_single_function":
            return interface.run_single_command(args[0])

        elif fn_name == "reset":
            return interface.sourceModel.reset()

        elif fn_name == "delete_source":
            if len(args) > 0:
                return interface.sourceModel.remove(args[0])
            else:
                return interface.sourceModel.remove(args[0])

        elif fn_name == "add_source":
            return interface.sourceModel.add()

        elif fn_name == "update_source":
            return interface.update()


        raise ValueError("Invalid Command")
    except Exception as e:
        error(str(e))
