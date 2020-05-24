"""
Commands that write bits of code that is valid for multiple languages
"""

from talon.voice import Context, Key
from ..utils import word

ctx = Context("general_lang")

ctx.keymap(
    {
        # Operators
        "(op equals | assign)": " = ",
        "greater than": " > ",
        "less than": " < ",
        "is equal to": " == ",
        # Completed matchables
        "call": ["()", Key("left")],
        "call brace": ["{}", Key("left")],
        "index": ["[]", Key("left")],
        # Statements
        "state (def | deaf | deft)": "def ",
        "state if": "if ",
        "state else if": [" else if ()", Key("left")],
        "state while": ["while ()", Key("left")],
        "state for": "for ",
        "state switch": ["switch ()", Key("left")],
        "state case": ["case \nbreak;", Key("up")],
        # Other Keywords
        # NPM
        # "(note | node) run": "npm run ",
        # "(note | node) start": ["npm start ", Key("enter")],
        # "(note | node) just": "npm run jest -- ",
        # "(note | node) type": ["npm run typecheck-dev", Key('enter')],
        # "screenshot": Key("ctrl-cmd-shift-4"),
        "vee eye ": "vim ",
        # "make <dgnwords>": ["make ", word],
        # "copy menu": Key('alt-cmd-c')
    }
)
