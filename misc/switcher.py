from .. import utils
from talon.voice import Word, Key, Context, Str, press
from talon.voice import Context
from talon import ui
import time
import os

running = {}
launch = {}

PREFIX = "pay"


def switch_app(m=None, name=None):
    if name is None:
        name = str(m["switcher.running"][0])

    full = running.get(name)
    if not full:
        return
    for app in ui.apps():
        if app.name == full:
            app.focus()
            # TODO: replace sleep with a check to see when it is in foreground
            time.sleep(0.25)
            break


def launch_app(m):
    name = str(m["switcher.launch"][0])
    path = launch.get(name)
    if path:
        ui.launch(path=path)


ctx = Context("switcher")
ctx.keymap(
    {
        "focus {switcher.running}": switch_app,
        "launch {switcher.launch}": launch_app,
        # custom switchers here
        "madam": lambda x: switch_app(x, "Atom"),
        PREFIX + " chrome": lambda x: switch_app(x, "Google Chrome"),
        PREFIX + " type": lambda x: switch_app(x, "Typora"),
        PREFIX + " kay": lambda x: switch_app(x, "Firefox"),
        # PREFIX + " kay": lambda x: switch_app(x, "Google Chrome"),
        PREFIX + " spotify": lambda x: switch_app(x, "Spotify"),
        PREFIX + " audacity": lambda x: switch_app(x, "Audacity"),
        PREFIX + " outlook": lambda x: switch_app(x, "Outlook"),
        PREFIX + " slack": lambda x: switch_app(x, "Slack"),
        PREFIX + " zulip": lambda x: switch_app(x, "Zulip"),
        PREFIX + " ableton": lambda x: switch_app(x, "Live "),
        PREFIX
        + " (console | counsel | consul | term | terminal)": lambda x: switch_app(
            x, "iTerm2"
        ),
        PREFIX + " messages": lambda x: switch_app(x, "Messages"),
        PREFIX + " (sub|sublime)": lambda x: switch_app(x, "Sublime Text"),
        PREFIX + " numbers": lambda x: switch_app(x, "Numbers"),
        PREFIX + " skype": lambda x: switch_app(x, "Skype for Business"),
        PREFIX + " marta": lambda x: switch_app(x, "Marta"),
        PREFIX + " signal": lambda x: switch_app(x, "Signal"),
        PREFIX + " messenger": lambda x: switch_app(x, "Messenger"),
        PREFIX + " quicktime": lambda x: switch_app(x, "QuickTime"),
        PREFIX + " imovie": lambda x: switch_app(x, "iMovie"),
        PREFIX + " kindle": lambda x: switch_app(x, "Kindle"),
        PREFIX + " zoom": lambda x: switch_app(x, "zoom.us"),
        PREFIX + " code": lambda x: switch_app(x, "Code"),
        PREFIX + " merge": lambda x: switch_app(x, "Sublime Merge"),
        PREFIX + " postman": lambda x: switch_app(x, "Postman"),
        PREFIX + " discord": lambda x: switch_app(x, "Discord"),
        PREFIX + " finder": lambda x: switch_app(x, "Finder"),
        PREFIX + " maestro": lambda x: switch_app(x, "Keyboard Maestro"),
        PREFIX + " simulator": lambda x: switch_app(x, "Simulator"),
        "system preferences": lambda x: switch_app(x, "System Preferences"),
        # custom switch macros
        PREFIX
        + " peter": [
            Key("cmd-s"),
            lambda x: switch_app(x, "iTerm2"),
            utils.delay(0.1),
            Key("up enter"),
        ],
        PREFIX
        + " micky": [
            Key("cmd-s"),
            lambda x: switch_app(x, "iTerm2"),
            utils.delay(0.1),
            Key("ctrl-c"),
            Key("up enter"),
        ],
    }
)


def update_lists():
    global running
    global launch
    new = {}
    for app in ui.apps():
        if app.background and not app.windows():
            continue
        words = app.name.split(" ")
        for word in words:
            if word and word not in new:
                new[word] = app.name
        new[app.name] = app.name
    running = new
    ctx.set_list("running", running.keys())

    new = {}
    for base in "/Applications", "/Applications/Utilities":
        for name in os.listdir(base):
            path = os.path.join(base, name)
            name = name.rsplit(".", 1)[0]
            new[name] = path
            words = name.split(" ")
            for word in words:
                if word and word not in new:
                    if len(name) > 6 and len(word) < 3:
                        continue
                    new[word] = path
    launch = new
    ctx.set_list("launch", launch.keys())


def ui_event(event, arg):
    if event in ("app_activate", "app_launch", "app_close", "win_open", "win_close"):
        # print(event, arg)
        if event in ("win_open", "win_closed"):
            if arg.app.name == "Amethyst":
                return
        update_lists()


ui.register("", ui_event)
update_lists()
