from talon import app, clip, cron, resource
from talon.voice import Context, Str, press, Key
from talon.webview import Webview
from ..misc.basic_keys import digits

from ..utils import parse_word
import os

########################################################################
# global settings
########################################################################

cwd = os.path.dirname(os.path.realpath(__file__))
########################################################################

context = Context("cd")
pick_context = Context("pickcd")

dirs = {
    "talon community": "$HOME/.talon/user/talon_community",
    "leetcode": "$HOME/projects/cake/lc",
    "golang directory": "$HOME/projects/go/src/github.com/slin63",
    "chronic pizza": "$HOME/projects/go/src/github.com/slin63/quickstart",
    "knoppers.icu": "$HOME/projects/go/src/github.com/slin63/knoppers.icu",
    "* projects": "$HOME/projects",
    "* downloads": "$HOME/Downloads",
    "* screenshots": "$HOME/Documents/Screenshots",
    "* desktop": "$HOME/Desktop",
    "* photos": "$HOME/Pictures",
}

active_word_list = None

webview = Webview()
css_template = """
<style type="text/css">
body {
    padding: 0;
    margin: 0;
    font-size: 150%;
    min-width: 600px;
}

td {
    text-align: left;
    margin: 0;
    padding: 5px 10px;
}

h3 {
    padding: 5px 0px;
}

table {
    counter-reset: rowNumber;
}

table .count {
    counter-increment: rowNumber;
}

.count td:first-child::after {
    content: counter(rowNumber);
    min-with: 1em;
    margin-right: 0.5em;
}

.pick {
    font-weight: normal;
    font-style: italic;
}

.cancel {
    text-align: center;
}

</style>
"""

dirs_template = (
    css_template
    + """
<div class="contents">
<h3>dirs</h3>
<table>
{% for dir in dirs %}
<tr class="count"><td class="pick">🔊 pick </td><td>{{ dir }}</td></tr>
{% endfor %}
<tr><td colspan="2" class="pick cancel">🔊 cancel</td></tr>
</table>
</div>
"""
)


def close_directories():
    webview.hide()
    pick_context.unload()


def make_selection(m):
    cron.after("0s", close_directories)
    words = m._words
    d = None
    if len(words) == 1:
        d = int(parse_word(words[0]))
    else:
        d = int(parse_word(words[1]))
    w = active_word_list[d - 1]

    cd_statement = f"cd {dirs[w]} && ls"
    insert(cd_statement)


def insert(cd_statement):
    press("ctrl-c", wait=0)
    Str(cd_statement)(None)
    press("enter", wait=0)


def get_selection():
    with clip.capture() as s:
        press("cmd-c", wait=0)
    return s.get()


def raise_directories(force_raise=False):
    global pick_context
    global active_word_list

    active_word_list = list(dirs.keys())

    valid_indices = range(len(active_word_list))

    webview.render(dirs_template, dirs=active_word_list)
    webview.show()

    keymap = {"(cancel | 0)": lambda x: close_directories()}

    keymap.update(
        {"[pick] %s" % (i + 1): lambda m: make_selection(m) for i in valid_indices}
    )

    pick_context.keymap(keymap)
    pick_context.load()


PREFIX = "(a | 8)"
context.keymap(
    {
        f"{PREFIX} cd": raise_directories,
        f"{PREFIX} edit": [f"subl {cwd}/cd.py:20", Key("enter")],
    }
)
