import os
import re

from random import choice

from talon.voice import Context, press, Key
from atomicwrites import atomic_write

from talon import app, webview
from talon.engine import engine
from talon_init import TALON_HOME

from talon.voice import Context

ctx = Context("last_phrase")

path = os.path.join(TALON_HOME, "last_phrase")
WEBVIEW = False
NOTIFY = True

IGNORE_PHRASES = [
    "notify toggle",
    "talon mode",
    "talon sleep",
    "dragon mode",
    "talon wake",
]

BIRDS = "🦉".split()


if WEBVIEW:
    webview = webview.Webview()
    webview.body = "<i>[waiting&nbsp;for&nbsp;phrase]</i>"
    webview.show()


def parse_phrase(phrase):
    return " ".join(word.split("\\")[0] for word in phrase)


def on_phrase(j):
    # context_name = j.get("parsed") or ""
    # if context_name:
    #     context_name = cleanup_context_name(context_name[0]._name)
    # print(
    #     "@6e6 ~/.talon/user/talon_community/misc/last_phrase.py:42\n>",
    #     f"j['parsed']: {cleanup_context_name(x[0]._name)}",
    # )
    phrase = parse_phrase(j.get("phrase", []))
    cmd = j["cmd"]
    if cmd == "p.end" and phrase:
        with atomic_write(path, overwrite=True) as f:
            f.write(phrase)

    if WEBVIEW and cmd in ("p.end", "p.hypothesis") and phrase:
        body = phrase.replace(" ", "&nbsp;")
        if cmd == "p.hypothesis":
            webview.render("<i>{{ phrase }}</i>", phrase=body)
        else:
            webview.render("{{ phrase }}", phrase=body)

    if NOTIFY and cmd == "p.end" and phrase and phrase not in IGNORE_PHRASES:
        app.notify(title=BIRDS[0], body=phrase)


def cleanup_context_name(name: str) -> str:
    name = re.sub("_+$", "", name)
    name = re.sub("keymap_+", "", name)
    print(name.strip())
    return name


engine.register("phrase", on_phrase)


def toggle_notify(m):
    global NOTIFY
    NOTIFY = not NOTIFY
    icon = "✅ Notifications on"
    if not NOTIFY:
        icon = "❌ Notifications off"
    app.notify(body=f"{icon}")


ctx.keymap({"notify toggle": toggle_notify})
