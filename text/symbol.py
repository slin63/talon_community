from talon.voice import Context, Key

ctx = Context("symbol")

keymap = {
    # simple
    "(question [mark] | questo)": "?",
    "plus": "+",
    "tilde": "~",
    "(bang | exclamation point | clamor)": "!",
    "(dollar [sign] | dolly)": "$",
    "(underscore | downscore | crunder)": "_",
    "colon": ":",
    "( [left] paren | precorp )": "(",
    "(rparen | are paren | right paren | precose)": ")",
    "(brace | braces | left brace | kirksorp)": "{",
    "(rbrace | are brace | right brace | kirkos)": "}",
    "(angle | left angle | less than)": "<",
    "(rangle | are angle | right angle | greater than)": ">",
    "(star | asterisk)": "*",
    "pound": "#",
    "percent [sign]": "%",
    "carrot": "^",
    "at sign": "@",
    "(and sign | ampersand | amper)": "&",
    "(pipe | spike)": "|",
    "(dubquote | double quote | double quotes | quatches)": '"',
    # compound
    "triple quote": "'''",
    "triple tick": "```",
    "[forward] dubslash": "//",
    "coal twice": "::",
    "(dot dot | dotdot)": "..",
    "(ellipsis | dot dot dot | dotdotdot)": "...",
    # unnecessary: use repetition commands?
}

ctx.keymap(keymap)
