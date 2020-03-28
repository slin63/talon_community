from datetime import datetime

from talon.voice import Context, Key, press, Str
from ..utils import (
    parse_words_as_integer,
    repeat_function,
    optional_numerals,
    text,
    delay,
)

context = Context("Typora", bundle="abnerworks.Typora")

context.keymap(
    {
        # Navigation
        "master [<dgndictation>]": [Key('cmd-shift-o'), text],
        "toggle sidebar": Key('shift-cmd-l'),
        "toggle outline": Key('ctrl-cmd-1'),

        # Formatting
        "italy": Key('cmd-i'),
        "bold": Key('cmd-b'),
        "code": Key('ctrl-`'),


        # Links
        "add link": Key('cmd-k'),

        # Views
        "view source": Key('cmd-/'),

        # Features
        "add line": Key('alt-cmd--'),
        "add code": Key('alt-cmd-c'),
    }
)
