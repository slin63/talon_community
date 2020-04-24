from talon.voice import Context, press, Key

"""

"""

from talon.voice import Context

ctx = Context(f"words")
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
    "fuck",
    "fucking",
    "fucked",
    "shit",
    "spotify",
    "unix",
    "linux",
    "inline",
    "crontab",
]

PREFIX = "(word | bit)"

ctx.keymap(
    {
        # special {PREFIX}
        "myemail": "shean.lin2018@gmail.com",
        f"{PREFIX} lynnex": "linux",
        f"{PREFIX} cron": "crontab",
        f"{PREFIX} (in 1 | in 9)": "inline",
        f"{PREFIX} mark": "mock",
        f"{PREFIX} queue": "queue",
        f"{PREFIX} eye": "eye",
        f"{PREFIX} bson": "bson",
        f"{PREFIX} iter": "iter",
        f"{PREFIX} cmd": "cmd",
        f"{PREFIX} dup": "dup",
        f"{PREFIX} (dickt | dictionary)": "dict",
        f"{PREFIX} shell": "shell",
        f"{PREFIX} talon": "talon",
        f"{PREFIX} eye pie": "ipython",
        f"{PREFIX} pie": "python",
        f"{PREFIX} pie 3": "python3.7 ",
        f"{PREFIX} eye pie": "ipython",
        f"{PREFIX} reddit": "reddit",
        f"{PREFIX} youtube": "youtube",
        f"{PREFIX} (jetlab | gitlab)": "gitlab",
        f"{PREFIX} jetignore": "gitignore",
        f"{PREFIX} (jethub | github)": "github",
        f"{PREFIX} in": "in",
        f"{PREFIX} Google calendar": "google calendar",
        f"{PREFIX} gmail": "gmail.com",
        "how about you": "hbu",
        f"{PREFIX} sequel": "sql",
        f"{PREFIX} sean": "Shean",
        f"{PREFIX} (lynn | lin)": "Lin",
        f"{PREFIX} my name": "Shean Lin",
        # Python library specific
        f"{PREFIX} canonical": "canonical",
        f"{PREFIX} (bullying | boolean)": "boolean",
        f"{PREFIX} google calendar": "https://calendar.google.com/calendar/r",
        f"{PREFIX} jason": "json",
        f"{PREFIX} toodo": "TODO: ",
        f"{PREFIX} dot eye and eye": ".ini",
        f"{PREFIX} localhost": "localhost:",
        f"{PREFIX} debugger": "debugger;",
        f"{PREFIX} views": "views",
        f"{PREFIX} postgres": "postgres",
        f"{PREFIX} pie test": "pytest ",
        f"{PREFIX} pippinv": "pipenv ",
        f"{PREFIX} daytime": "datetime",
        f"{PREFIX} delete": "delete",
        f"{PREFIX} oopsy": "error",
        "( {PREFIX} counsel | {PREFIX} consul )": "console",
        f"{PREFIX} olympic": "alembic",
        f"{PREFIX} bootstrap": "bootstrap",
        f"{PREFIX} jaydee": "jwt",
        f"{PREFIX} feeflag": "feature flag",
        f"{PREFIX} goday": "golang",
        f"{PREFIX} string": "string",
        f"{PREFIX} bite": "byte",
        f"{PREFIX} rpc": "RPC",
        f"{PREFIX} pid": "PID",
        f"{PREFIX} (indy | index)": "index",
        f"{PREFIX} riff": "raft",
        f"{PREFIX} cord": "chord",
        f"{PREFIX} noppers": "knoppers",
        f"{PREFIX} gist": "gist",
        f"{PREFIX} IP": "IP",
    }
)
