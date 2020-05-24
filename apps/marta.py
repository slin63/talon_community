from datetime import datetime

from talon.voice import Context, Key, press, Str
from ..utils import (
    parse_words_as_integer,
    repeat_function,
    optional_numerals,
    text,
    delay,
)

context = Context("Marta", bundle="org.yanex.marta")

context.keymap(
    {
        "(go to file|master) [<dgndictation>]": [Key("cmd-p"), text],
        "command [<dgndictation>]": [Key("cmd-shift-p"), text],
        "toggle terminal": Key("alt-cmd-o"),
    }
)
