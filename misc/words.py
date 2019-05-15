from talon.voice import Context, press, Key
"""

"""

from talon.voice import Context

ctx = Context("words")

ctx.keymap(
    {
        "word queue": "queue",
        "word eye": "eye",
        "word bson": "bson",
        "word iter": "iter",
        "word cmd": "cmd",
        "word dup": "dup",
        "word (dickt | dictionary)": "dict",
        "word shell": "shell",
        "word talon": "talon",
        "word eye pie": "ipython",
        "word pie": "python",
        "word pie 3": "python3.7 ",
        "word eye pie": "ipython",
        "word reddit": "reddit",
        "word youtube": "youtube",
        "word (jetlab | gitlab)": "gitlab",
        "word (jethub | github)": "github",
        "word in": "in",
        "Word Google calendar": "google calendar",
        "word gmail": "gmail.com",
        "how about you": "hbu",
        "word sequel": "sql",
        "word sean": "Shean",
        "word lin": "Lin",
        "word my name": "Shean Lin",
        # Python library specific
        "word dbs": "DBSession",
        "word nosetest": "nosetests",
        "word canonical": "canonical",
        "word dockshell": "dockshell",
        "word geebizz": "gbiz",
        "word geegeebiz": ["[GBIZ-]", Key("left")],
        "word (bullying | boolean)": "boolean",
        "word google calendar": "https://calendar.google.com/calendar/r",
        "word jason": "json",
        "word toodo": "# TODO: ",
        "word dot eye and eye": ".ini",
        "word localhost": "localhost:",
        "word debugger": "debugger;",
        "word views": "views",
        "word gee dev": "https://us.dev.app.granular.ag",
        "word postgres": "postgres",
        "word connection string": "psql -h localhost -U alpine_webapp -d granular",
        "word password": "501second",
    }
)
