from talon.voice import Key, press, Str, Context
from talon.webview import Webview
from talon import app, clip, cron, resource
from ..utils import parse_word

ctx = Context("clipboard")
pick_context = Context("clipboardpick")

CLIPBOARD_DEFAULT = ["crontab"]
CLIPBOARD = CLIPBOARD_DEFAULT.copy()

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

template = (
    css_template
    + """
<div class="contents">
<h3>clipboard</h3>
<table>
{% for v in data %}
<tr class="count"><td class="pick">🔊 </td><td><code>{{ v }}</code></td></tr>
{% endfor %}
<tr><td colspan="2" class="pick cancel">🔊 cancel</td></tr>
</table>
</div>
"""
)


def close_directories():
    webview.hide()
    pick_context.unload()


def set_selection(m):
    with clip.capture() as sel:
        press("cmd-c")
    print("sel:", sel.get())
    value = sel.get()
    if value not in CLIPBOARD:
        CLIPBOARD.append(value)
    clip.set(value)


def make_selection(m):
    cron.after("0s", close_directories)
    words = m._words
    print("CLIPBOARD:", CLIPBOARD)
    d = None
    if len(words) == 1:
        d = int(parse_word(words[0]))
    else:
        d = int(parse_word(words[1]))
    w = CLIPBOARD[d - 1]

    Str(w)(None)


def get_selection(m):
    valid_indices = range(len(CLIPBOARD))

    webview.render(template, data=CLIPBOARD)
    webview.show()

    keymap = {"(cancel | 0)": lambda x: close_directories()}

    keymap.update(
        {"[pick] %s" % (i + 1): lambda m: make_selection(m) for i in valid_indices}
    )

    pick_context.keymap(keymap)
    pick_context.load()


def clear_clipboard(_):
    global CLIPBOARD
    CLIPBOARD = CLIPBOARD_DEFAULT.copy()


PREFIX = "(a | 8)"
keymap = {
    f"{PREFIX} paste": get_selection,
    f"{PREFIX} clip": set_selection,
    f"{PREFIX} clear": clear_clipboard,
}

ctx.keymap(keymap)
