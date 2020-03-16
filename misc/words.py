from talon.voice import Context, press, Key

"""

"""

from talon.voice import Context

ctx = Context("words")
ctx.vocab = [
    "photocrop",
    "liveness",
    "uncomment",
    "mock",
    "async",
    "alembic",
    "kubernetes",
    "mutex",
    "semaphore",
    "recurse",
    "fuck", "fucking", "fucked",
    "spotify"
]

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
        "word (lynn | lin)": "Lin",
        "word my name": "Shean Lin",
        # Python library specific
        "word canonical": "canonical",
        "word dockshell": "dockshell",
        "word (bullying | boolean)": "boolean",
        "word google calendar": "https://calendar.google.com/calendar/r",
        "word jason": "json",
        "word toodo": "TODO: ",
        "word dot eye and eye": ".ini",
        "word localhost": "localhost:",
        "word debugger": "debugger;",
        "word views": "views",
        "word postgres": "postgres",
        "word pie test": "pytest ",
        "word pippinv": "pipenv ",
        "word daytime": "datetime",
        "word delete": "delete",
        "word oopsy": "error",
        "( word counsel | word consul )": "console",
        "word olympic": "alembic",
        "word bootstrap": "bootstrap",
        "word jaydee": "jwt",
        "word feeflag": "feature flag",
        "word goday": "golang",
        "word string": "string",
        "word bite": "byte",
        "word rpc": "RPC",
        "word pid": "PID",
        "word (indy | index)": "index",
        "word riff": "raft",
        "word cord": "chord",
        "word noppers": "knoppers",
    }
)
