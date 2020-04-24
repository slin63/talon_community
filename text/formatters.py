from talon.voice import Word, Context, press
from talon import clip

from ..utils import (
    insert,
    laugh,
    normalise_keys,
    parse_word,
    surround,
    text,
    sentence_text,
    word,
    parse_words,
    camel_case,
    spoken_text,
    snake_text,
    dot_text,
    caps_text
)

PREFIX = ""


def title_case_capitalize_word(index, word, _):
    words_to_keep_lowercase = "a,an,the,at,by,for,in,of,on,to,up,and,as,but,or,nor".split(
        ","
    )
    if index == 0 or word not in words_to_keep_lowercase:
        return word.capitalize()
    else:
        return word


formatters = normalise_keys(
    {
        # ""tree": (True, lambda i, word, _: word[0:3] if i == 0 else ""),"
        # "quad": (True, lambda i, word, _: word[0:4] if i == 0 else ""),
        # PREFIX + "camel": (
        #     True,
        #     lambda i, word, _: word if i == 0 else word.capitalize(),
        # ),
        # PREFIX + "pathway": (True, lambda i, word, _: word if i == 0 else "/" + word),
        # PREFIX + "dotsway": (True, lambda i, word, _: word if i == 0 else "." + word),
        # PREFIX + "yellsmash": (True, lambda i, word, _: word.upper()),
        PREFIX + "(yeller)": (False, lambda i, word, _: word.upper()),
        PREFIX + "(lower)": (False, lambda i, word, _: word.lower()),
        # PREFIX + "yellsnik": (
        #     True,
        #     lambda i, word, _: word.upper() if i == 0 else "_" + word.upper(),
        # ),
        # "dollcram": (
        #     True,
        #     lambda i, word, _: "$" + word if i == 0 else word.capitalize(),
        # ),
        # PREFIX + "champ": (True, lambda i, word, _: word.capitalize() if i == 0 else " " + word),
        # "lowcram": (
        #     True,
        #     lambda i, word, _: "@" + word if i == 0 else word.capitalize(),
        # ),
        # "(criff | criffed)": (True, lambda i, word, _: word.capitalize()),
        # "tridal": (False, lambda i, word, _: word.capitalize()),
        # "snake": (True, lambda i, word, _: word if i == 0 else "_" + word),
        # PREFIX + "dotsnik": (True, lambda i, word, _: "." + word if i == 0 else "_" + word),
        # PREFIX + "smash": (True, lambda i, word, _: word),
        # "(spine | kebab)": (True, lambda i, word, _: word if i == 0 else "-" + word),
        PREFIX + "title": (False, title_case_capitalize_word),
    }
)

# surrounders = normalise_keys(
#     {
#         PREFIX + "(dubstring | coif)": (False, surround('"')),
#         PREFIX + "(string | posh)": (False, surround("'")),
#         PREFIX + "(tics | glitch)": (False, surround("`")),
#         PREFIX + "padded": (False, surround(" ")),
#         PREFIX + "dunder": (False, surround("__ ")),
#          + "brax": (False, surround("[", "]")),
#         PREFIX + "kirk": (False, surround("{", "}")),
#         PREFIX + "precoif": (False, surround('("', '")')),
#         PREFIX + "(prex | args)": (False, surround("(", ")")),
#     }
# )

# formatters.update(surrounders)


def FormatText(m):
    fmt = []

    for w in m._words:
        if isinstance(w, Word) and w != "over":
            fmt.append(w.word)
    words = parse_words(m)
    if not words:
        try:
            with clip.capture() as s:
                press("cmd-c")
            words = s.get().split(" ")
        except clip.NoChange:
            words = [""]

    tmp = []

    smash = False
    for i, w in enumerate(words):
        word = parse_word(w, True)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words) - 1)
        tmp.append(word)

    sep = "" if smash else " "
    insert(sep.join(tmp))
    # if no words, move cursor inside surrounders
    if not words[0]:
        for i in range(len(tmp[0]) // 2):
            press("left")


ctx = Context("formatters")

ctx.keymap(
    {
        "(phrase | say) <dgndictation> [over]": text,
        # "saturn <dgndictation> waffle stomp": text,
        "sentence <dgndictation> [over]": sentence_text,
        "(comma | ,) <dgndictation> [over]": [", ", spoken_text],
        "period <dgndictation> [over]": [". ", sentence_text],
        "word <dgnwords>": word,
        "slash <dgnwords>": ["/", word],
        "dash <dgnwords>": ["-", word],
        "snake <dgndictation>": snake_text,
        "camel <dgndictation>": camel_case,
        # "point <dgndictation>": dot_text,
        "laugh": laugh,
        "capital <dgndictation>": caps_text,
        "(%s)+ [<dgndictation>] over" % (" | ".join(formatters)): FormatText,
    }
)
