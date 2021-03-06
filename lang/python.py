from talon.voice import Context, Key

from ..utils import is_filetype, snake_text, caps_text

FILETYPES = (".py",)
PYTHON_ALIAS = "( pie | pipe )"

ctx = Context("python")

# ctx = Context("python", func=is_filetype(FILETYPES))

ctx.keymap(
    {
        "state any": ["any()", Key("left")],
        PYTHON_ALIAS + " initial": "__init__",
        "dot pie": ".py",
        "dot pipe": ".py",
        "self assign <dgndictation> [over]": [
            "self.",
            snake_text,
            " = ",
            snake_text,
            "\n",
        ],
        "star arguments": "*args",
        "star star Kwargs": "**kwargs",

        # Shortcuts for structures
        PYTHON_ALIAS + " ( class | plus ) <dgndictation> over": [
            "class ",
            caps_text,
            "():",
            "\n"
        ],
        PYTHON_ALIAS + " ( funk | fuck | fox ) <dgndictation> over": [
            "def ",
            snake_text,
            "():",
            Key("left left")
        ],

        # Functions
        PYTHON_ALIAS + " ( funk | fuck | fox ) <dgndictation> self over": [
            "def ",
            snake_text,
            "(self, ):",
            Key("left left")
        ],
        PYTHON_ALIAS + " ( call | caw ) <dgndictation>": [
            snake_text,
            "()",
            Key("left")
        ],

        # Logic and control flow
        PYTHON_ALIAS + " if [<dgndictation>] ": [
            "if ",
            snake_text,
            ":",
            Key("left")
        ],
        PYTHON_ALIAS + " if not [<dgndictation>] ": [
            "if not ",
            snake_text,
            ":",
            Key("left")
        ],
        PYTHON_ALIAS + " elif [<dgndictation>] ": [
            "elif ",
            snake_text,
            ":",
            Key("left")
        ],
        PYTHON_ALIAS + " else": [
            "else:",
        ],

        PYTHON_ALIAS + " ( 4 | for ) [<dgndictation>] in [over]": [
            "for ",
            snake_text,
            " in :",
            Key("left")
        ],
        PYTHON_ALIAS + " while [<dgndictation>] [over]": [
            "while ",
            snake_text,
            ":",
            Key("left")
        ],

        # Keywords
        PYTHON_ALIAS + " pass": "pass",
        PYTHON_ALIAS + " assert": "assert",
        # PYTHON_ALIAS + " break": "break",
        PYTHON_ALIAS + " none": "None",
        PYTHON_ALIAS + " true": "True",
        PYTHON_ALIAS + " false": "False",
        PYTHON_ALIAS + " self dot": "self.",
        "pirate": "return ",
        PYTHON_ALIAS + " under": "__",
        PYTHON_ALIAS + " repper": "__repr__",
        PYTHON_ALIAS + " not": "not",
        PYTHON_ALIAS + " import [<dgndictation>] ": [
            "import ",
            snake_text,
        ],
        PYTHON_ALIAS + " from [<dgndictation>] ": [
            "from ",
            snake_text,
        ],


        # Objects
        PYTHON_ALIAS + " tuple": "()",
        PYTHON_ALIAS + " list": "[]",
        PYTHON_ALIAS + " ( tick | dict | dick )": "{}",

        # Shortcuts
        PYTHON_ALIAS + " peepee": "from pprint import pprint as pp",
        PYTHON_ALIAS + " com": ", ",
        PYTHON_ALIAS + " ( tick | dict | dick ) assign": [
            "[] = ",
            Key("left left left left")
        ],
        PYTHON_ALIAS + " keys": [".keys()", Key('enter')],
        PYTHON_ALIAS + " (decorate | decorator)": "@",
        PYTHON_ALIAS + " fixture": "@pytest.fixture",
        PYTHON_ALIAS + " default": "=None",
        PYTHON_ALIAS + " type": " -> ",
        PYTHON_ALIAS + " dundick": ".__dict__",
        PYTHON_ALIAS + " set": "=",
        PYTHON_ALIAS + " break": Key("ctrl-shift-b "),
        PYTHON_ALIAS + " block": ["()", Key("left enter enter shift-tab up tab")],
        PYTHON_ALIAS + " argument": [Key("cmd-right"), ",", Key("enter")],
        PYTHON_ALIAS + " dock": ["\"\"\"\"\"\"", Key("left left left")],
        PYTHON_ALIAS + " print": ["print()", Key("left")]
    }
)
