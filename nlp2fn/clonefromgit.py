import os, json
from nlp2fn.git import Repo
from nlp2fn.utils import update_py_fnc_dir
from nlp2fn.utils.colorpriniting import error

def GitEvents(link):
    if len(link.split("/")[-1].split(".")) > 1:
        error ("Invalid Link :" + link)
        return

    PATH = os.path.expanduser("~/.nlp2fnsource")
    repoconf = os.path.join(PATH, link.split("/")[-1])
    if not os.path.exists(repoconf):
        os.makedirs(repoconf)

    repo = Repo(repoconf)
    repo.clone(link)

    if os.path.exists(os.path.join(repoconf, "nlp2fn.events.json")):
        with open(os.path.join(repoconf, "nlp2fn.events.json"), 'r') as f:
            data = json.load(f)
        update_py_fnc_dir(os.path.join(repoconf, data["events"]))
    else:
        print (os.path.join(repoconf, "nlp2fn.events.json"), "does not exits")
