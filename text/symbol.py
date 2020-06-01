from talon.voice import Context, Key

ctx = Context("symbol")

keymap = {
    # simple
    "(question [mark])": "?",
    "plus": "+",
    "tilde": "~",
    "(bang)": "!",
    "dollar": "$",
    # "(underscore | crunder)": "_",
    "( [left] paren )": "(",
    "(rparen | are paren | right paren)": ")",
    "(brace | braces | left brace)": "{",
    "(rbrace | are brace | right brace)": "}",
    "(angle | left angle | less than)": "<",
    "(rangle | are angle | right angle | greater than)": ">",
    "(star | asterisk)": "*",
    "pound": "#",
    "percent": "%",
    "carrot": "^",
    "at sign": "@",
    "(and sign | ampersand | amper)": "&",
    "(pipe)": "|",
    "(dubquote | double quote | double quotes)": '"',
    # compound
    "triple quote": "'''",
    "triple tick": "```",
}

ctx.keymap(keymap)
