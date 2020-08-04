from talon.voice import Context, Key, press
import talon.clip as clip
from ..utils import (
    text,
    parse_words,
    parse_words_as_integer,
    insert,
    word,
    join_words,
    is_filetype,
)

context = Context("javascript_meta")
PREFIX = "java"

context.keymap(
    {
        f"{PREFIX} package [<dgndictation>]": ["npm ", text, ""],
        f"{PREFIX} plex [<dgndictation>]": ["npx ", text, ""],
        f"{PREFIX} version [<dgndictation>]": ["nvm ", text, ""],
        f"{PREFIX} yarn [<dgndictation>]": ["yarn ", text, ""],
    }
)
