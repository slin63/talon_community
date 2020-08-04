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

JS_EXTENSIONS = (".js", ".jsx", ".ts", ".tsx")

# context = Context("javascript", func=is_filetype(JS_EXTENSIONS))
context = Context("javascript")
PREFIX = "java"


def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = " ".join(words)
    s = s.replace(" – ", "-")
    insert(s)


def CursorText(s):
    left, right = s.split("{.}", 1)
    return [left + right, Key(" ".join(["left"] * len(right)))]


context.keymap(
    {
        f"{PREFIX} const [<dgndictation>]": ["const ", text],
        f"{PREFIX} let [<dgndictation>]": ["let ", text],
        f"{PREFIX} arrow": " => ",
        f"{PREFIX} print": ["console.log()", Key("left")],
        f"{PREFIX} trip": " === ",
    }
)
