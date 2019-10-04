from talon.voice import Context, Key

from ..utils import is_filetype, snake_text, caps_text

FILETYPES = (".go",)
PYTHON_ALIAS = "( pie | pipe )"
GO_ALIAS = "gogo"

ctx = Context("go", func=is_filetype(FILETYPES))


ctx.keymap(
    {
        "state any": ["any()", Key("left")],
        "pirate": "return ",
        "coal sign": " := ",
        "go var": "var ",
        "go amp": "&",
        "go format": "fmt",


        PYTHON_ALIAS + " set": "=",
        PYTHON_ALIAS + " argument": [Key("cmd-right"), ",", Key("enter")],

    }
)
