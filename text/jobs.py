from talon.voice import Key, press, Str, Context
from talon.webview import Webview
from talon import app, clip, cron, resource
from ..utils import parse_word

from datetime import datetime

ctx = Context("jobs")
pick_context = Context("jobspick")
date = datetime.now().strftime("%m/%d/%Y")

recurse = """
- Studied distributed systems, Golang, and concurrency at self-directed programming sabbatical.
- Implemented a distributed file system, consensus module, and membership system, while also blogging about their mechanics and the process of implementing them.
- Created AWS-hosted programmatically generated web gallery (knoppers.icu) to host photography, as well as a blog (chronicpizza.net) to host technical and creative writing projects.
- Presented project progress and interesting findings to peers at weekly talks.
"""
granular = """
- Separated legacy Python2.7 codebase into Python3.7 microservices, allowing teams to work on individual dockerized services without building a monolithic codebase, saving many hours of wasted developer time.
- Created a Google- maps style landing page, replacing the functionality of several legacy pages and streamlining user experience.
- Reused or built Python / Flask APIs and React components and their accompanying unit tests.
- Wrote and explained SQL queries to product managers to quantify user behaviors and prioritize new feature development.
"""
dod = """
- Converted storm modeling codebase from Excel VBA to C# and reduced runtime by 93%.
- Redesigned SQL schema to implement web caching for C#-Silverlight application.
- Created Python scripts for trend analysis of arbitrarily large time-series datasets.
"""

CLIPBOARD_DEFAULT = [
    "shean.lin2018@gmail.com",
    date,
    "5104957455",
    "412 W Washington St",
    "Shean Lin",
    "https://www.linkedin.com/in/sheanlin-fsd/",
    "https://github.com/slin63",
    "https://www.chronicpizza.net/",
    "https://www.chronicpizza.net/tags/tech/",
    "http://knoppers.icu/",
    recurse,
    granular,
    dod,
]
CLIPBOARD = CLIPBOARD_DEFAULT.copy()

webview = Webview()
css_template = """
<style type="text/css">
body {
    padding: 0;
    margin: 0;
    font-size: 160%;
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
    font-family: Arial, Helvetica, sans-serif;
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
<tr class="count"><td class="pick">🔊 </td><td>{{ v[0:50] }}</td></tr>
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


PREFIX = "(job)"
keymap = {
    f"{PREFIX} paste": get_selection,
}

ctx.keymap(keymap)
