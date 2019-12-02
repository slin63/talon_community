from talon.voice import Context, Key

from ..utils import is_filetype, snake_text, caps_text, camel_case, text

FILETYPES = (".go",)
PYTHON_ALIAS = "( pie | pipe )"
GO_ALIAS = "go"

# ctx = Context("go", func=is_filetype(FILETYPES))
ctx = Context("go")
ctx.vocab = [
    "goroutine",
    "nil",
    "golang",
    "waitgroup"
]



ctx.keymap(
    {
        "state any": ["any()", Key("left")],
        "pirate": "return ",

        # Symbols
        "coal sign": " := ",
        GO_ALIAS + " chan": "chan ",
        GO_ALIAS + " var": "var ",
        GO_ALIAS + " make": ["make()", Key('left')],
        GO_ALIAS + " print": ["fmt.Println()", Key('left')],
        GO_ALIAS + " fee print": ["fmt.Printf()", Key('left')],
        GO_ALIAS + " amp": "&",
        GO_ALIAS + " format": "fmt",
        GO_ALIAS + " range": "range ",
        GO_ALIAS + " arrow": " <- ",
        GO_ALIAS + " arrow short": "<-",
        GO_ALIAS + " map": ["map[]", Key('left')],

        # Goroutines
        GO_ALIAS + " go [<dgndictation>]": [
            "go ",
            text
        ],

        # Structures
        GO_ALIAS + " struct <dgndictation> over": [
            "type ",
            caps_text,
            " struct {"
        ],

        # Interfaces
        GO_ALIAS + " interface <dgndictation> over": [
            "type ",
            caps_text,
            " interface {"
        ],

        # Logic and control flow
        GO_ALIAS + " if [<dgndictation>] ": [
            "if ",
            camel_case,
            " {"
        ],



        GO_ALIAS + " set": "=",
        GO_ALIAS + " argument": [Key("cmd-right"), ",", Key("enter")],
        GO_ALIAS + " ( funk | fuck | fox ) <dgndictation> over": [
            "func ",
            camel_case,
            "() {",
        ],
    }
)
