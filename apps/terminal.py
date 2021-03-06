import time
import time
import json

from talon.voice import Word, Key, Context, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
from talon import ctrl, ui, resource
import string

from ..utils import numerals, parse_words, text, is_in_bundles, insert, snake_text, word
from ..bundle_groups import TERMINAL_BUNDLES

# TODO: move application specific commands into their own files: apt-get, etc

ctx = Context("terminal", func=is_in_bundles(TERMINAL_BUNDLES))

mapping = {"semicolon": ";", r"new-line": "\n", r"new-paragraph": "\n\n"}


def parse_word(word):
    word = word.lstrip("\\").split("\\", 1)[0]
    word = mapping.get(word, word)
    return word


def dash(m):
    words = parse_words(m)
    press(" ")
    if len(words) == 1 and len(words[0]) == 1:
        press("-")
        Str(words[0])(None)
    else:
        press("-")
        press("-")
        Str("-".join(words))(None)


def jump_tab(m):
    tab_number = utils.parse_words_as_integer(m._words[1:])
    if tab_number is not None and tab_number > 0 and tab_number < 9:
        press("option-%s" % tab_number)


KUBERNETES_PREFIX = "(cube | cube control)"
SHELL_PREFIX = "she"

try:
    servers = json.load(resource.open("servers.json"))
except Exception as e:
    print(f"error opening servers.json: {e}")
    servers = {}


def get_server(m):
    return servers[" ".join(m["global_terminal.servers"])]


def mosh_servers(m):
    insert(f"mosh {get_server(m)}")


def ssh_servers(m):
    insert(f"ssh {get_server(m)}")


def name_servers(m):
    insert(get_server(m))


def ssh_copy_id_servers(m):
    insert(f"mosh {get_server(m)}")


def new_server(m):
    press("cmd-d")
    insert(f"ssh {get_server(m)}")
    press("enter")


keymap = {
    "town logs": 'tail -f "/Users/seanlin/.talon/talon.log"',
    "SHE Whereami": "pwd ",
    "SHE home": "~/",
    "SHE history": ["fc -l", Key("enter")],
    # generic editor stuff
    "lefty": Key("ctrl-a"),
    "ricky": Key("ctrl-e"),
    "snip": Key("ctrl-u"),
    "snip right": Key("ctrl-k"),
    "fame": Key("ctrl-left"),
    "famie": Key("ctrl-w"),
    "fish": Key("ctrl-right"),
    "(snatch)": Key("cmd-x"),
    "(stish)": Key("cmd-c"),
    "(spark)": Key("cmd-v"),
    "(select all | olly | ali)": Key("cmd-a"),
    "fuck this": Key("ctrl-d"),
    "(pain new | split vertical)": Key("cmd-d"),
    "new {global_terminal.servers}": new_server,
    # talon
    "tail talon": "tail -f ~/.talon/talon.log",
    "talon reple": "~/.talon/bin/repl",
    # some habits die hard
    "troll char": Key("ctrl-c"),
    "reverse": Key("ctrl-r"),
    "change [<dgnwords>]": [
        "cd ",
        word,
        "; ls",
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
    ],
    "change up": ["cd ..; ls", Key("enter")],
    "cd wild": [
        "cd **; ls",
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
    ],
    "cd wild [<dgndictation>]": [
        "cd **; ls",
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        text,
    ],
    "(ls | run ellis | run alice)": "ls\n",
    "(la | run la)": "ls -la\n",
    # "durrup": "cd ..; ls\n",
    "go back": "cd -\n",
    "dash <dgndictation> [over]": dash,
    "pseudo": "sudo ",
    "(redo pseudo | pseudo [make me a] sandwich)": [
        Key("up"),
        Key("ctrl-a"),
        "sudo ",
        Key("enter"),
    ],
    "SHE C H mod": "chmod ",
    "SHE clear": [Key("ctrl-c"), "clear\n"],
    # "SHE copy [<dgndictation>]": ["cp ", text],
    # "SHE copy (recursive | curse) [<dgndictation>]": ["cp -r", text],
    "SHE kill": Key("ctrl-c"),
    "SHE list [<dgndictation>]": ["ls ", text],
    "SHE list all [<dgndictation>]": ["ls -la ", text],
    "SHE make (durr | dear | directory) [<dgndictation>]": ["mkdir ", text],
    "SHE mipple [<dgndictation>]": ["mkdir -p ", text],
    "SHE move [<dgndictation>]": ["mv ", text],
    "SHE remove [<dgndictation>]": ["rm ", text],
    "SHE remove (recursive | curse) [<dgndictation>]": ["rm -rf ", text],
    "SHE enter": "ag -l | entr ",
    "SHE enter 1": "ag -l . .. | entr ",
    "SHE enter 2": "ag -l . ../.. | entr ",
    "SHE less [<dgndictation>]": ["less ", text],
    "SHE cat [<dgndictation>]": ["cat ", text],
    "SHE X args [<dgndictation>]": ["xargs ", text],
    "SHE mosh": "mosh ",
    "SHE mosh {global_terminal.servers}": mosh_servers,
    "SHE SSH {global_terminal.servers}": ssh_servers,
    # "SHE server {terminal.servers}": name_servers,
    "SHE SSH copy id {global_terminal.servers}": ssh_copy_id_servers,
    "SHE M player": "mplayer ",
    "SHE nvidia S M I": "nvidia-smi ",
    "SHE R sync": "./src/dotfiles/sync_rsync ",
    "SHE tail": "tail ",
    "SHE tail follow": "tail -f ",
    "shall count lines": "wc -l ",
    # python
    "create virtual environment": ["virtualenv -p python3 venv", Key("enter")],
    "activate virtual environment": [
        "source `find . | grep bin/activate$`",
        Key("enter"),
    ],
    # apt-get
    "apt get": "apt-get ",
    "apt get install": "apt-get install ",
    "apt get update": "apt-get update ",
    "apt get upgrade": "apt-get upgrade ",
    # Tools
    "SHE (grep | grip)": "grep ",
    "pee socks": "ps aux ",
    "vi": "vim ",
    # python
    "piepie": "pipenv",
    "piepie run": "pipenv run",
    "piepie deploy": "pipenv run deploy/tools/server",
    "piepie shell": "pipenv shell",
    "piepie stall": "pipenv install",
    "pip install": "pip install ",
    "pip install requirements": "pip install -r ",
    "pip install editable": "pip install -e ",
    "pip install this": "pip install -e .",
    "pip install local": "pip install -e .",
    "pip [install] upgrade": "pip install --upgrade ",
    "pip uninstall": "pip uninstall ",
    "pip list": "pip list",
    "toolbelt": Key("cmd-shift-b"),
    "SHE top": ["htop", Key("enter")],
    "fuck him up": [Key("f9"), Key("enter")],
    # kubectl
    KUBERNETES_PREFIX + "control": "kubectl ",
    KUBERNETES_PREFIX + "create": "kubectl create ",
    KUBERNETES_PREFIX + "expose": "kubectl expose ",
    KUBERNETES_PREFIX + "run": "kubectl run ",
    KUBERNETES_PREFIX + "set": "kubectl set ",
    KUBERNETES_PREFIX + "run-container": "kubectl run-container ",
    KUBERNETES_PREFIX + "get": "kubectl get ",
    KUBERNETES_PREFIX + "explain": "kubectl explain ",
    KUBERNETES_PREFIX + "edit": "kubectl edit ",
    KUBERNETES_PREFIX + "delete": "kubectl delete ",
    KUBERNETES_PREFIX + "rollout": "kubectl rollout ",
    KUBERNETES_PREFIX + "rolling-update": "kubectl rolling-update ",
    KUBERNETES_PREFIX + "scale": "kubectl scale ",
    KUBERNETES_PREFIX + "autoscale": "kubectl autoscale ",
    KUBERNETES_PREFIX + "certificate": "kubectl certificate ",
    KUBERNETES_PREFIX + "cluster-info": "kubectl cluster-info ",
    KUBERNETES_PREFIX + "top": "kubectl top ",
    KUBERNETES_PREFIX + "cordon": "kubectl cordon ",
    KUBERNETES_PREFIX + "uncordon": "kubectl uncordon ",
    KUBERNETES_PREFIX + "drain": "kubectl drain ",
    KUBERNETES_PREFIX + "taint": "kubectl taint ",
    KUBERNETES_PREFIX + "describe": "kubectl describe ",
    KUBERNETES_PREFIX + "logs": "kubectl logs ",
    KUBERNETES_PREFIX + "attach": "kubectl attach ",
    KUBERNETES_PREFIX + "exec": "kubectl exec ",
    KUBERNETES_PREFIX + "port-forward": "kubectl port-forward ",
    KUBERNETES_PREFIX + "proxy": "kubectl proxy ",
    KUBERNETES_PREFIX + "cp": "kubectl cp ",
    KUBERNETES_PREFIX + "auth": "kubectl auth ",
    KUBERNETES_PREFIX + "apply": "kubectl apply ",
    KUBERNETES_PREFIX + "patch": "kubectl patch ",
    KUBERNETES_PREFIX + "replace": "kubectl replace ",
    KUBERNETES_PREFIX + "convert": "kubectl convert ",
    KUBERNETES_PREFIX + "label": "kubectl label ",
    KUBERNETES_PREFIX + "annotate": "kubectl annotate ",
    KUBERNETES_PREFIX + "completion": "kubectl completion ",
    KUBERNETES_PREFIX + "api": "kubectl api ",
    KUBERNETES_PREFIX + "config": "kubectl config ",
    KUBERNETES_PREFIX + "help": "kubectl help ",
    KUBERNETES_PREFIX + "plugin": "kubectl plugin ",
    KUBERNETES_PREFIX + "version": "kubectl version ",
    KUBERNETES_PREFIX
    + "shell": ["kubectl exec -it  -- /bin/bash"]
    + [Key("left")] * 13,
    # conda
    "conda install": "conda install ",
    "conda list": "conda list ",
    # tmux
    "T mux new session": "tmux ",
    "T mux scroll": [Key("ctrl-b"), Key("[")],
    # other
    "SHE make": "make\n",
    "SHE jobs": "jobs\n",
    "SHE copy": "| pbcopy",
    "SHE paste": "pbpaste >> ",
    "SHE copy last": "echo !! | pbcopy",
    "SHE again": [Key("up enter")],
    "SHE code": ["code .", Key("enter")],
    "swampy": Key("cmd-left"),
    # sql
    "pity [<dgndictation>]": ["\d+ ", snake_text],
    "connect granular [<dgndictation>]": ["brocdb gran ", snake_text],
    "connect data warehouse [<dgndictation>]": ["brocdb adw ", snake_text],
    "pexecute [<dgndictation>]": ["\i ", text],
    "pee fit": ["\\x auto", Key("enter")],
    "pee tables": "\dt ",
    "gottem": [Key("right"), Key("enter")],
    "merge": ["smerge .", Key("enter")],
    "jar (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8)": jump_tab,
    "gee dash": "gb-",
    "flaky": ["flake8", Key("enter")],
    "gogo [<dgndictation>]": ["go ", text],
    "gogo run [<dgndictation>]": ["go run ", text],
    "sequel csv": "sqltocsv ",
    # sublime
    "sub": ["subl .", Key("enter")],
    # hugo
    "hugo [<dgndictation>]": ["hugo ", text],
    "SHE get directory": ["echo $(pwd)| pbcopy", Key("enter")],
    "SHE google": ["google $(pbpaste)", Key("enter")],
    "SHE rebuild": [Key("ctrl-c"), Key("up"), Key("enter")],
    "SHE echo": "echo ",
    "SHE gore": ["gore", Key("enter")],
    "SHE noise": ["noise", Key("enter")],
    # Pretty && Rich History
    "pretty drum": ["dh", Key("enter")],
    "pretty harp": ["ph", Key("enter")],
    # Other stuff
    SHELL_PREFIX + " tomato": ["nohup pomo -g  &> /dev/null &", Key("left " * 15)],
    SHELL_PREFIX + " curl": ["curl ",],
}

for action in ("get", "delete", "describe"):
    for object in ("nodes", "jobs", "pods", "namespaces", "services", "events", ""):
        if object:
            object = object + " "
        command = f"{KUBERNETES_PREFIX} {action} {object}"
        typed = f"kubectl {action} {object}"
        keymap.update({command: typed})

keymap.update({"(pain | bang) " + str(i): Key("alt-" + str(i)) for i in range(10)})

ctx.keymap(keymap)


def shell_rerun(m):
    # switch_app(name='iTerm2')
    app = ui.apps(bundle="com.googlecode.iterm2")[0]
    ctrl.key_press("c", ctrl=True, app=app)
    time.sleep(0.05)
    ctrl.key_press("up", app=app)
    ctrl.key_press("enter", app=app)


global_ctx = Context("global_terminal")
global_ctx.keymap(
    {"SHE rerun": shell_rerun, "SHE server {global_terminal.servers}": name_servers}
)
global_ctx.set_list("servers", servers.keys())
# module.exports = {
#   permissions: "chmod "
#   access: "chmod "
#   ownership: "chown "
#   "change own": "chown "
#   "change group": "chgrp "
#   cat: "cat "
#   chat: "cat " # dragon doesn't like the word 'cat'
#   copy: "cp "
#   "copy recursive": "cp -r "
#   move: "mv "
#   remove: "rm "
#   "remove recursive": "rm -rf "
#   "remove directory": "rmdir "
#   "make directory": "mkdir "
#   link: "ln "
#   man: "man "
#   list: "ls "
#   "list all": "ls -al "
#   ls: "ls "
#
#   "python reformat": "yapf -i "
#   "enter": "ag -l | entr "
#   "enter to": "ag -l . ../.. | entr "
# }
